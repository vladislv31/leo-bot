from bot import bot
from bot import messages
from config import configs
from bot import keyboards
from bot.keyboards import make_keyboard
from bot.database import Db
from bot import settings


@bot.message_handler(func=lambda m: m.text == 'Старт/Стоп')
def run_bot(m):
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

    msg = bot.send_message(cid, messages.manage_menu, reply_markup=keyboards.run)
    bot.register_next_step_handler(msg, run_menu, pin)

def run_menu(m, pin):
    cid = m.chat.id
    text = m.text

    run_commands = {
        'RUNBULL': 'BUYBTC',
        'RUNBEAR': 'SELLBTC',
        'STOP': 'STOP'
    }

    if text in run_commands.keys():
        command = str(pin) + run_commands[text]
        bot.send_message(cid, 'Команда успешно выполнена', reply_markup=keyboards.main)
        bot.send_message(cid, command)
    else:
        bot.send_message(cid, messages.start, reply_markup=keyboards.main)
        

