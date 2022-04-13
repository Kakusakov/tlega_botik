import telebot as tb
tok = open("token.txt", "r")
bot = tb.TeleBot(token=tok.read())
tok.close()