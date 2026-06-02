import os
import models as m

def get_my_ip_adress()->str: return os.popen("hostname -I").read().split()[0]

def print_class(course:int)->str: return "класс" if course>=9 else "курс"

def validate(email:str)->bool: return any(i.email == email for i in m.User.select_user())