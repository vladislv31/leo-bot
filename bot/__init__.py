from telebot import TeleBot
import config


bot = TeleBot(config.TOKEN)

from bot.handlers import general
from bot.handlers import connect_bot
from bot.handlers import manage_bot
from bot.handlers import admin
