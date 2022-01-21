
import threading
from function import *
import admin

class reg (threading.Thread):
   def __init__(self, my_id, ran, users, logins,):
       threading.Thread.__init__(self)
       self.threadID = my_id
       self.id = my_id
       self.random = ran
       self.users = users
       self.logins = logins
       self.reg = reg
   def run(self):
    reg = True
    req = True
    while reg:
        if self.users.get(self.id, 0) == 0:
            write_msg(self.id, "Выполните вход\n "
                             "Учитель|Ученик|админ\n"
                             "гений|дурак|бог", self.random)
        random, my_id, login = get_msg()
        while not (login.lower() == "учитель" or login.lower() == "ученик" or login.lower() == "админ"):
            write_msg(my_id, "Введите пользователя", random)
            random, my_id, login = get_msg()

        write_msg(my_id, "Пароль:", random)
        random, my_id, password = get_msg()
        if login.lower() == "админ" and password == 'бог':
            write_msg(my_id, 'Пользователь подтверждён', random)
            self.users[my_id] = 1
            self.logins[my_id] = "admin"
            login = " "
            reg = False
        if login.lower() == "учитель" and password == 'гений':
            write_msg(my_id, 'Пользователь подтверждён', random)
            self.users[my_id] = 1
            self.logins[my_id] = "teacher"
            login = " "
            reg = False
        if login.lower() == "ученик" and password == 'дурак':
            write_msg(my_id, 'Пользователь подтверждён', random)
            self.users[my_id] = 1
            self.logins[my_id] = "student"
            login = " "
            reg = False

    while req:
        if self.logins[self.id] == "admin":
            print(1)
            S = admin.admin(self.id, self.random)
            req = False
