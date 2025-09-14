'''Основной модуль, реализующий взаимодействие пользователя с ботом внутри тг'''
import telebot
from telebot import types
from functools import partial

'''Функция начала общения, ответ на команду /start'''
class Bot:
    '''Функция сетапит переменную из main'''
    def setup(self, bot):

        @bot.message_handler(commands = ['start']) #обработчик команды старт
        def send_welcome(message):
            welcome_text = """
Приветствую, Мастер! 

Я твой верный помощник в настольных приключениях. Я могу создать случайного NPC, бросить вызов героям новым квестом или найти для них сокровища в древней гробнице.

Используй /help, чтобы увидеть все мои способности.
"""
            bot.reply_to(message, welcome_text)