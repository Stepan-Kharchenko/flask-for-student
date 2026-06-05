from flask import Flask,request,render_template
import models as m

def initialize(app:Flask):
    @app.route("/test",methods=["GET"])
    def selecttest():
        def get_exersize_id(var:int):
            return (i.exersize_id for i in m.Results.select_test([m.Results.variant == var]))
        mail = request.args.get("email")
        user_id = m.User.select_user([m.User.email==mail])[0].id
        d,variants = {},{i.variant for i in m.Results.select_test([user_id == m.Results.user_id,
                                                                   m.Results.ball==-1])}
        math_themes = ("Алгебра","Геометрия","Вероятность и Статистика")
        physic_themes = ("Механика","МКТ и Термодинамика","Электромагнетизм","Квантовая")
        for i in variants:
            if all(m.Study.select_exersize(id).theme in math_themes for id in get_exersize_id(i)):
                d[i]="Математика"
            elif all(m.Study.select_exersize(id).theme in physic_themes for id in get_exersize_id(i)):
                d[i]="Физика"
            else: d[i]="Гибрид"
        print(d)
        return render_template("test/start.html",dct=d,email=mail)
    
    @app.route("/test/go",methods=["POST","GET"])
    def gotest():
        var,mail = request.form["variant"],request.args.get("email")
        user = m.User.select_user([m.User.email == mail])[0]
        ids = {i.id for i in m.Results.select_test([m.Results.variant==var, m.Results.user_id==user.id])}
        return render_template("test/test.html",ids=tuple(ids),email=mail,m=m)
    
    @app.route("/test/test",methods=["POST","GET"])
    def endtest():
        mail,answers,count = request.args.get("email"),request.form,0
        true_answers = {int(i[6:]): m.Study.select_exersize(m.Results.select_test([m.Results.exersize_id==int(i[6:])])[0].exersize_id).answer for i in answers}
        for i in answers:
            with m.Session() as session:
                result = session.query(m.Results).get(int(i[6:]))
                print(result.ball)
                if result.ball==-1:
                    res = int(answers[i] == true_answers[int(i[6:])])
                    result.ball,count = res,count+res
                    session.commit()
                else: raise ValueError("result in table")
        return f"У вас {count} из {len(answers)} правильных ответов<br><a href='/'>Главная</a>"