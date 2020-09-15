from bot import bot
from bot import messages
from config import configs
from bot import keyboards
from bot.keyboards import make_keyboard
from bot.database import Db
from bot import settings


@bot.message_handler(func=lambda m: m.text == 'Управление ботом')
def manage_bot(m):
    cid = m.chat.id
    msg = bot.send_message(cid, messages.enter_pin, reply_markup=keyboards.hide)
    bot.register_next_step_handler(msg, enter_pin)

def enter_pin(m):
    cid = m.chat.id
    pin = m.text

    db = Db()

    config_id = db.check_pin(pin)

    if config_id:
        user_id = db.get_user_id(cid)
        if not db.get_used_config(user_id, config_id):
            bot.send_message(cid, messages.pin_error, reply_markup=keyboards.main)
            return
    else:
        bot.send_message(cid, messages.pin_error, reply_markup=keyboards.main)
        return

    db.close()

    msg = bot.send_message(cid, messages.manage_menu, reply_markup=keyboards.manage)
    bot.register_next_step_handler(msg, manage_menu, pin)

def manage_menu(m, pin):
    cid = m.chat.id
    text = m.text

    if text == 'Размер контрактов':
        msg = bot.send_message(cid, 'Тут можно изменить размер контракта', reply_markup=make_keyboard([['Изменить', 'Назад']]))
        bot.register_next_step_handler(msg, change_contract, pin)
    else:
        bot.send_message(cid, messages.start, reply_markup=keyboards.main)

def change_contract(m, pin):
    cid = m.chat.id
    text = m.text

    if text == 'Изменить':
        msg = bot.send_message(cid, 'Укажите новый контракт:', reply_markup=keyboards.hide)
        bot.register_next_step_handler(msg, new_contract, pin)
    else:
        bot.send_message(cid, messages.start, reply_markup=keyboards.main)

def new_contract(m, pin):
    cid = m.chat.id
    new_contract = m.text

    bot.send_message(cid, 'Контракт изменен!', reply_markup=keyboards.main)
    bot.send_message(cid, settings.change_command.format(pin, new_contract))










