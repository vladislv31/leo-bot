from bot import bot
from bot import messages
from bot import keyboards
from bot.database import Db
from config import ADMIN_ID


def check_id(func):
    def wrapper(m):
        cid = m.chat.id
        if cid != ADMIN_ID:
            from bot.handlers.general import start
            start(m)
            return
        func(m)
    return wrapper


@bot.message_handler(commands=['admin'])
@check_id
def get_id(m):
    cid = m.chat.id
    bot.send_message(cid, messages.admin, reply_markup=keyboards.admin)

@bot.message_handler(func=lambda m: m.text == 'Список свободных конфигов')
@check_id
def free_configs(m):
    cid = m.chat.id
    db = Db()
    configs = db.get_free_configs()
    db.close()
    
    reply = ''

    for i in configs:
        reply += f'{i["title"]} - {i["descr"]} - {i["pin"]}\n'

    bot.send_message(cid, messages.free_configs + '\n\n' + reply)

@bot.message_handler(func=lambda m: m.text == 'Добавить конфиг')
@check_id
def get_id(m):
    cid = m.chat.id
    msg = bot.send_message(cid, messages.enter_config_name, reply_markup=keyboards.hide)
    bot.register_next_step_handler(msg, config_name)

def config_name(m):
    cid = m.chat.id
    name = m.text

    data = {}
    data['name'] = name

    msg = bot.send_message(cid, messages.enter_config_descr)
    bot.register_next_step_handler(msg, config_descr, data)

def config_descr(m, data):
    cid = m.chat.id
    descr = m.text

    data['descr'] = descr

    msg = bot.send_message(cid, messages.enter_pin)
    bot.register_next_step_handler(msg, config_pin, data)

def config_pin(m, data):
    cid = m.chat.id
    pin = m.text

    data['pin'] = pin

    reply = f'Название: {data["name"]}\nОписание: {data["descr"]}\nPIN: {data["pin"]}'

    msg = bot.send_message(cid, messages.check_data + '\n\n' + reply, reply_markup=keyboards.check_data)
    bot.register_next_step_handler(msg, check_config_data, data)

def check_config_data(m, data):
    cid = m.chat.id
    text = m.text

    if text == 'Сохранить':
        db = Db()
        new_conf = db.new_config(data['name'], data['descr'], data['pin'])
        if not new_conf is True:
            bot.send_message(cid, new_conf, reply_markup=keyboards.admin)
        else:
            bot.send_message(cid, messages.admin, reply_markup=keyboards.admin)
        db.close()
    else:
        bot.send_message(cid, messages.admin, reply_markup=keyboards.admin)












