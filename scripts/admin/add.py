from flask import Flask,render_template,request
import models as m

def initialize(app:Flask):
    @app.route("/admin/add_exersize",methods=["POST"])
    def add():
        subject = request.form["subject"]
        return render_template("admin/add_exersize.html",subject=subject)
    
    @app.route("/admin/add_exersize/end",methods=["POST"])
    def endadd():
        d = dict(request.form)
        d["study_class"] = d["class"]
        del d["class"]
        indexs = (i.index for i in m.Study.select_exersize([m.Study.theme == d["theme"]]))
        print(indexs)
        try: maxind = max(indexs)
        except ValueError: maxind = 0
        print(d,maxind)
        m.Study.add_exersize(**d,
                             math=(d["theme"] in ("Алгебра","Геометрия","Вероятность и Статистика")),
                             index=maxind+1)
        return render_template("admin/add_end.html")