import os
import telebot

#from telebot import apihelper
API_TOKEN = '1111494654:AAFGfe1jLP5A1JD79hSeM-97y4wVbzToFGo'

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_message(message):
    bot.reply_to(message, "hello")

@bot.message_handler(commands=['photo'])
def send_welcome(message):
    os.system('./crphoto.sh')
    photo = open('1.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)
    os.system('./dphoto.sh')
    
# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

#879159087
bot.polling()
