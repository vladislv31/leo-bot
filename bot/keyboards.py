from telebot import types


def make_keyboard(rows):
    keyboard = types.ReplyKeyboardMarkup(True, False)
    
    for r in rows:
        keyboard.row(*r)

    return keyboard


main = make_keyboard([['Подключить бота', 'Управление ботом', 'Старт/Стоп']])
manage = make_keyboard([['Размер контрактов', 'Назад']])
contract_sizes = make_keyboard([['20', '100', '500']])
admin = make_keyboard([['Список свободных конфигов'], ['Добавить конфиг', 'Назад']])
check_data = make_keyboard([['Сохранить', 'Назад']])
run = make_keyboard([['RUNBULL', 'RUNBEAR', 'STOP'], ['Назад']])
hide = types.ReplyKeyboardRemove()
