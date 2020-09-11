from bot import bot
from bot import messages
from config import configs
from bot.keyboards import make_keyboard
from bot import keyboards
from bot import settings
from bot.database import Db


@bot.message_handler(func=lambda m: m.text == 'Подключить бота')
def connect_bot(m):
    cid = m.chat.id
    db = Db()
    configs = db.get_free_configs()
    db.close()
    
    reply = ''

    for i in configs:
        reply += f'{i["id"]} - {i["title"]} - {i["descr"]}\n'

    msg = bot.send_message(cid, messages.choose_config + '\n\n' + reply, reply_markup=keyboards.hide)
    bot.register_next_step_handler(msg, choose_config)


def choose_config(m):
    cid = m.chat.id
    config = m.text

    data = {}
    data['config'] = config

    bot.send_message(cid, messages.connect_instruction, reply_markup=keyboards.hide)
    msg = bot.send_message(cid, messages.enter_id_key)
    bot.register_next_step_handler(msg, enter_id_key, data)

def enter_id_key(m, data):
    cid = m.chat.id
    id_key = m.text

    data['id_key'] = id_key

    msg = bot.send_message(cid, messages.enter_secret_key)
    bot.register_next_step_handler(msg, enter_secret_key, data)

def enter_secret_key(m, data):
    cid = m.chat.id
    secret_key = m.text

    data['secret_key'] = secret_key

    msg = bot.send_message(cid, messages.enter_base_size)
    bot.register_next_step_handler(msg, enter_base_size, data)

def enter_base_size(m, data):
    cid = m.chat.id
    base_size = m.text

    data['base_size'] = base_size

    msg = bot.send_message(cid, messages.check_data, reply_markup=keyboards.check_data)
    bot.register_next_step_handler(msg, check_connect_data, data)

    #bot.send_message(cid, settings.add_command.format('123', data['id_key'], data['base_size'], data['config'], data['secret_key']))

def check_connect_data(m, data):
    cid = m.chat.id
    text = m.text

    if text == 'Сохранить':
        db = Db()

        user_id = db.get_user_id(cid)
        db.connect_config(user_id, data['config'])

        db.close()

        bot.send_message(cid, messages.start, reply_markup=keyboards.main)
    else:
        bot.send_message(cid, messages.start, reply_markup=keyboards.main)








