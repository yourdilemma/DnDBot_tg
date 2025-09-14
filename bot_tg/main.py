import telebot
import json
import random
import bot_tg.dungeon_master_bot as dungeon_master_bot

with open("bot_tg/config.json","r") as file: #скрываем токен
    config = json.load(file)
    api_token = config["api_token"]

bot=telebot.TeleBot(api_token)
bot_handler = dungeon_master_bot.Bot()        
bot_handler.setup(bot)

bot.polling(none_stop=True, interval=0) #обновляем данные о работе бота