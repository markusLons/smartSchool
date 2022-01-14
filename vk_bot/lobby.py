from admin import *



users = dict()
logins = dict()
reg = True
req = True
while True:
    while reg:
        text = 0
        while text == 0:
            random, my_id, text = read_msg()
        if users.get(my_id, 0) == 0:
            write_msg(my_id, "Выполните вход\n "
                             "Учитель|Ученик|админ\n"
                             "гений|дурак|adm", random)
            random, my_id, login = get_msg()
            while not (login.lower() == "учитель" or login.lower() == "ученик" or login.lower() == "админ"):
                write_msg(my_id, "Введите пользователя", random)
                random, my_id, login = get_msg()

            write_msg(my_id, "Пароль:", random)
            random, my_id, password = get_msg()
            if login.lower() == "учитель" and password == 'гений':
                write_msg(my_id, 'Пользователь подтверждён', random)
                users[my_id] = 1
                logins[my_id] = "teacher"
                login = 0
                reg = False
            elif login.lower() == "ученик" and password == 'дурак':
                write_msg(my_id, 'Пользователь подтверждён', random)
                users[my_id] = 1
                logins[my_id] = "student"
                login = 0
                reg = False
            elif login.lower == "админ" and password == "бог":
                write_msg(my_id, 'Пользователь подтверждён', random)
                users[my_id] = 1
                logins[my_id] = "admin"
                login = 0
                reg = False
    users[my_id] = 1
    print(1)
    while True:
        if logins[my_id] == "teacher":
            print(1)
            student = admin(my_id, random)