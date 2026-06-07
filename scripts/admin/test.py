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
                if i[:2]==val or (val=="st" and i=="root"): yield i
        d = request.form
        print(dict(d))
        for student in (sort(d,"st") if "root" not in dict(d) else ("root",)):
            uclass = m.Study.select_exersize(int(tuple(sort(d,"ex"))[0][2:])).study_class
            user_id = int(student[2:]) if student!="root" else m.User.select_user([m.User.user_class==uclass,
                                                                                   m.User.last_name=="root"])[0].id
            vars = [i.variant for i in m.Results.select_test([m.Results.user_id==user_id])]
            maxvar = 0 if not vars else max(vars)
            for exersize in sort(d,"ex"):
                exersize_id = int(exersize[2:])
                if student=="root":
                    user_id = m.User.select_user([m.User.last_name=="root",
                                                  m.User.user_class==m.Study.select_exersize\
                                                    (exersize_id).study_class])[0].id
                else: user_id=int(student[2:])
                print(user_id)
                user = m.User.select_user(user_id)
                m.Results.add_test(user_id=user_id,
                                   exersize_id=exersize_id,
                                   variant=maxvar+1)
        return render_template("admin/test_end.html")