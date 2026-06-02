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
    d = request.form
    print(d)
    return f"Спасибо, {d['surname']} {d['name']}. Ваша почта - {d['email']}"

if __name__ == "__main__":
    print("run")
    app.run(ip,debug=True)