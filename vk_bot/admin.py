from function import *
class admin( object):

    def __init__(self, my_id, random):
        self.id = my_id
        self.random = random

    def _thread(self):
        write_msg(id, "узнать расписание для любого класса - расписание"
                      "поменять расписание для любого класса - исправть расписание"
                      "выйти из аккаунта - выйти", random)
        random, id, event= get_msg()
        if event == 'расписание':
            write_msg(id, "првиет", random)
        else:
            write_msg(id, 'не то', random)
