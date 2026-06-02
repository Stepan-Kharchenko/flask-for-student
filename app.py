from flask import Flask
from flask import render_template,request

import utils as ut
import models as m
ip = ut.get_my_ip_adress()
app = Flask(__name__)
print(ip)

@app.route("/")
def first():
    print(request.remote_addr)
    return render_template("index.html")

@app.route("/registration")
def registration():
    return render_template("registration_forms.html")

@app.route("/registration/end",methods=["POST"])
def end_of_registration():
    d = dict(request.form)
    d["math"],d["physic"] = "math" in d, "physic" in d
    d["user_class"] = d["class"]
    del d["class"]
    m.User.add_user(**d)
    return f"Спасибо, {d['last_name']} {d['first_name']}. Ваши данные сохранены.|\
<a href='/'>Главная</a>"

if __name__ == "__main__":
    print("run")
    app.run(ip,debug=True)