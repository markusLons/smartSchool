from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
TOKEN = "2119125825:AAFuoIG77PETtemi6E93GkDKqJevsqQTmTM"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
login = 0
auth = 0
@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
   if msg.text.lower() == 'login':
       await msg.answer('Введите пароль')
       global login
       login = 1
       print(1)
   else:
       await msg.answer('введите логин')
       print(3)
print(login)
if login == 1:
    print(2)
    async def get_text_messages(msg: types.Message):
        if msg.text.lower() == 'password':
            await msg.answer('Вы успешно авторизировались')


if __name__ == '__main__':
   executor.start_polling(dp)