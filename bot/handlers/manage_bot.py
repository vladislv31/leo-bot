from bot import bot
from bot import messages
from config import configs
from bot import keyboards


@bot.message_handler(func=lambda m: m.text == 'Управление ботом')
def manage_bot(m):
    cid = m.chat.id
    msg = bot.send_message(cid, messages.enter_pin, reply_markup=keyboards.hide)
    bot.register_next_step_handler(msg, enter_pin)

def enter_pin(m):
    cid = m.chat.id
    pin = m.text

    msg = bot.send_message(cid, messages.manage_menu, reply_markup=keyboards.manage)
    bot.register_next_step_handler(msg, manage_menu)

def manage_menu(m):
    cid = m.chat.id
    text = m.text

    if text == 'Размер контрактов':
        bot.send_message(cid, 'Меняем контракт')
    else:
        bot.send_message(cid, messages.start, reply_markup=keyboards.main)










