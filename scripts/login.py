from flask import Flask,render_template,request
import utils as ut
import models as m

def initialize(app:Flask):
    @app.route("/registration")
    def registration(): return render_template("login/registration_forms.html")

    @app.route("/registration/end",methods=["POST"])
    def end_of_registration():
        try:
            d = dict(request.form)
            d["math"],d["physic"] = "math" in d, "physic" in d
            d["user_class"] = d["class"]
            del d["class"]
            m.User.add_user(**d)
            return f"Спасибо, {d['last_name']} {d['first_name']}. Ваши данные сохранены. | <a href='/'>Главная</a>"
        except ValueError as e: return "Пользователь с таким email уже существует | <a href='/'>Главная</a>"

    @app.route("/login")
    def login():
        return render_template("login/login.html")

    @app.route("/login/validation",methods=["GET"])
    def validation():
        mail = request.args.get("email")
        print(mail)
        return render_template("start.html",
                               validate=ut.validate(mail),
                               admin=ut.validate_admin(mail),
                               email=mail)