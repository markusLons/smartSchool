import threading
from function import *


def admin(id, random):
        write_msg(id, "узнать расписание для любого класса - расписание \n"
                      "поменять расписание для любого класса - исправть расписание\n"
                      "выйти из аккаунта - выйти", random)
        random, id, event= get_msg()
        if event == 'расписание':
            write_msg(id, "првиет", random)
        else:
            write_msg(id, 'не то', random)
