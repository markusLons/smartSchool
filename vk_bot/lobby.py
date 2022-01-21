import threading

from admin import admin
from reg import  reg
from function import *



users = dict()
logins = dict()

while True:
    text = 0
    while text == 0:
        random, my_id, text = read_msg()
    a = reg(my_id, random, users, logins,)
    a.start()
    a.join()
