from flask import Flask
import scripts.login as login
import scripts.admin as admin

def initialize(app:Flask):
    login.initialize(app)
    admin.initialize(app)
