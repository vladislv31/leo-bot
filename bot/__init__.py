from telebot import TeleBot
import config


bot = TeleBot(config.TOKEN)

from bot import handlers
