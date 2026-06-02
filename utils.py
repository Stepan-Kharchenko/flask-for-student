import os

def get_my_ip_adress()->str: return os.popen("hostname -I").read().split()[0]

def print_class(course:int)->str: return "класс" if course>=9 else "курс"