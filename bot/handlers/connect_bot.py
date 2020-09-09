from bot import bot
from bot import messages
from config import configs
from bot.keyboards import make_keyboard
from bot import keyboards
from bot import settings


@bot.message_handler(func=lambda m: m.text == 'Подключить бота')
def connect_bot(m):
    cid = m.chat.id
    msg = bot.send_message(cid, messages.choose_config, reply_markup=make_keyboard([configs]))
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

    bot.send_message(cid, settings.add_command.format('123', data['id_key'], data['base_size'], data['config'], data['secret_key']))









