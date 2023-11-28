#27 KIRILL-LOTIN TELEGRAM BOT

# Sodda telegram bot yaratamiz

# 1-QISM. KIRILL-LOTIN-KIRILL TRANSLITERATOR

from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = "6462840255:AAF-DMosleKC541avSqe6JoK8g5oVBWfh-Q"
bot = telebot.TeleBot(TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalom alaykum, Xush kelibsiz!"
    javob += "\nMatn kiriting: "
    bot.reply_to(message, javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
#     if msg.isascii():
#         javob = to_cyrillic(msg)
#     else:
#         javob = to_latin(msg)
    bot.reply_to(message, javob(msg))

bot.polling()

# matn = input("Matn kriting: ")
#
# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))

# 2-QISM. TELEGRAM BOT

