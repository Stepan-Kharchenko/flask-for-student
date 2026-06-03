from flask import Flask
import scripts.login as login

def initialize(app:Flask):
    login.initialize(app)