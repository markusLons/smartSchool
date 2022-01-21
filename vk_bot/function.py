import vk_api
import pymysql

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

con = ''
cursor = ''
def setConnect(host = 'svr3.educationhost.cloud',user='zyhhnxcz_students',password='Students1',db='zyhhnxcz_bank',charset='utf8mb4' ):
    global con
    con = pymysql.connect(host=host,
                          user=user,
                          password=password,
                          db=db,
                          charset=charset)
    global cursor
    cursor = con.cursor()
setConnect()
