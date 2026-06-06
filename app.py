from flask import Flask
from flask import render_template,request

import utils as ut
import models as m
import scripts
ip = ut.get_my_ip_adress()
app = Flask(__name__)
print(ip)

@app.route("/")
def first():
    print(request.remote_addr)
    return render_template("index.html")

scripts.initialize(app)

if __name__ == "__main__":
    print("run")
    app.run(host=ip,debug=True)