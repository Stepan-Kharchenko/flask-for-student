from flask import Flask,render_template
import scripts.admin.add as add

def initialize(app:Flask):
    @app.route("/admin")
    def admin():
        return render_template("admin/panel.html")
    
    add.initialize(app)