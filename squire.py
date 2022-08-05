import telebot
import os
import re
from DiceParser import DiceParser
from DiceParser import DICE_DELIMETERS

TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def dice_handler(message):
    try:
        if (re.match('^/[0-9]*' + DICE_DELIMETERS, message.text)):
            dp = DiceParser()
            dp.parse(message.text[1:])
            bot.reply_to(message, dp.getDescription())
    except:
        pass
bot.polling()
