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

    if len(configs) < 1:
        reply += 'Пусто...'

    msg = bot.send_message(cid, messages.choose_config + '\n\n' + reply, reply_markup=make_keyboard([['Отмена']]))
    bot.register_next_step_handler(msg, choose_config)


def choose_config(m):
    cid = m.chat.id
    config = m.text

    if config == 'Отмена':
        bot.send_message(cid, messages.start, reply_markup=keyboards.main)
        return

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

        if db.check_config(data['config']):
            user_id = db.get_user_id(cid)
            config = db.get_config(data['config'])
            db.connect_config(user_id, data['config'])
            bot.send_message(cid, messages.connect_success)
            bot.send_message(cid, 'PIN-код для конфига - ' + str(config['pin']), reply_markup=keyboards.main)
            bot.send_message(cid, settings.add_command.format(config['pin'], data['id_key'], data['base_size'], config['title'], data['secret_key']))
        else:
            bot.send_message(cid, messages.config_not_exists, keyboards.main)

        db.close()

    else:
        bot.send_message(cid, messages.start, reply_markup=keyboards.main)








