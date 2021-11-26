import time
import vk_api

vk = vk_api.VkApi(token='398d932966e344fc5a42f40c0856ab8dfd915efe6ffe919b83ccc3ac7d99351f73afcfda8c3051627a02e')

param = {
    'count': 1,
    'time_offset': 5,
    'filter': 'unread'
}


def write_msg(user_id, msg, random):
    vk.method('messages.send', {
        'user_id': user_id,
        'message': msg,
        'random_id': random
    })


def get_msg():
    text = 0
    my_id = 0
    random = 0
    while (text == 0):
        random, my_id, text = read_msg()
    return random, my_id, text


def read_msg():
    item1 = 0
    last_mess1 = 0
    random1 = 0
    my_id1 = 0
    text1 = 0
    response = vk.method('messages.getConversations', param)
    if response['items']:
        item = response['items'][0]
        last_mess = item['last_message']
        random1 = last_mess['random_id']
        my_id1 = last_mess['peer_id']
        text1 = last_mess['text']
    return random1, my_id1, text1


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
            while not (login.lower() == "учитель" or login.lower() == "ученик"):
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
            elif login.lower == "админ" and password == "adm":
                write_msg(my_id, 'Пользователь подтверждён', random)
                users[my_id] = 1
                logins[my_id] = "admin"
                login = 0
                reg = False

    write_msg(my_id, 'Выход – выйти из аккаунта \n '
                     'Расписание – узнать расписание\n '
                     'Поменять расписание – поменять урок в расписание', random)


    while req:
        if users[my_id] == "teacher":
            from teacher import *
        if  users[my_id] == "student":
            from student import *
    req = False
    reg = True

