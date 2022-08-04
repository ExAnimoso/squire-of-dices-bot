import telebot
import os

TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['bruh'])
def bruh_handler(message):
    bot.send_message(message.chat.id, 'BRUH')
bot.polling()
