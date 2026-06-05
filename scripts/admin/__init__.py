from flask import Flask,render_template
import scripts.admin.add as add
import scripts.admin.test as test
import models as m

def initialize(app:Flask):
    @app.route("/admin")
    def admin(): return render_template("admin/panel.html")
    add.initialize(app)
    test.initialize(app)
    @app.route("/admin/statistic")
    def statistic():
        def function(user,subject):
            #res = m.Results.select_test((m.Study.select_exersize((m.Results.exersize_id,))  == (subject=="math")\
            #                             and m.Results.user_id == user.id),)
            res = (i.ball for i in [] if i!=-1)
            print(res)
            return 0 #sum(res)/len(res) if res else 0
        def function2(exersize): return 0
        return render_template("admin/statistic.html",
                               users=m.User.select_user(),
                               exersizes=m.Study.select_exersize(),
                               f=function,f2=function2)
    