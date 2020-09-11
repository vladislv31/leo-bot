from bot import bot
from bot import messages
from bot import keyboards
from bot.database import Db


@bot.message_handler(commands=['start', 'help'])
@bot.message_handler(func=lambda m: m.text == 'Назад')
def start(m):
    cid = m.chat.id
    username = m.from_user.username

    db = Db()
    db.new_user(str(cid), username)
    db.close()

    bot.send_message(cid, messages.start, reply_markup=keyboards.main)

@bot.message_handler(commands=['get_id'])
def get_id(m):
    cid = m.chat.id
    bot.send_message(cid, str(cid))
