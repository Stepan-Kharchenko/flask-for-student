from flask import Flask
import scripts.login as login
import scripts.admin as admin
import scripts.test as test

def initialize(app:Flask):
    login.initialize(app)
    admin.initialize(app)
    test.initialize(app)
