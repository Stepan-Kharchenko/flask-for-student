from flask import Flask,request,render_template
import models as m

def initialize(app:Flask):
    @app.route("/admin/test",methods=["POST"])
    def test():
        d = request.form
        lmath = ("Алгебра","Геометрия","Вероятность и Статистика")
        lphys = ("Механика","МКТ и Термодинамика","Электромагнетизм","Квантовая")
        match d["subject"]:
            case "physic": l = lphys
            case "math": l = lmath
            case "gibrid": l = lmath+lphys
            case _: raise ValueError
        print(l)
        with m.Session() as session:
            exs = session.query(m.Study).filter(m.or_(m.Study.theme == i for i in l),
                                                m.Study.study_class == d["class"])
            users = m.User.select_user(([m.User.user_class==d["class"]]))
        return render_template("admin/add_test.html", exersizes=exs, users=users)
    
    @app.route("/admin/test/end",methods=["POST"])
    def end_test():
        def sort(dct:dict,val:str):
            for i in dct:
                if i[:2]==val: yield i
        d = request.form
        print(d)
        for student in sort(d,"st"):
            for exersize in sort(d,"ex"):
                user_id,exersize_id = int(student[2:]),int(exersize[2:])
                user = m.User.select_user(user_id)
                vars = [i.variant for i in m.Results.select_test([m.Results.user_id==user_id])]
                maxvar = 0 if not vars else max(vars)
                m.Results.add_test(user_id=user_id,
                                   exersize_id=exersize_id,
                                   variant=maxvar+1)
        return "Сохранено"