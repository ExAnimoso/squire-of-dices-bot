import telebot
import os
import random

TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def bruh_handler(message):
    if message.from_user.username == 'ExAnimoso':
        bot.send_message(message.chat.id, message.text + ' ' + str(random.randint(1, 20)))
    else:
        bot.send_message(message.chat.id, 'Возьми д20 в руки и брось на стол. Сообщи чату результат на верхней грани.')
bot.polling()
