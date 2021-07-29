import telebot

# http://t.me/Py_vapor_v2_bot

token = '1804065816:AAE0-UXoZG9kRqWa53D97Gii3DcLqov3rJk'

bot = telebot.TeleBot(token)

my_name = 'Sergey'


@bot.message_handler(content_types=["text"])
def echo(message):
    if my_name in message.text:
        text = 'Ба! Знакомые все лица'
    else:
        text = message.text
    bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)