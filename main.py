import traceback
from time import sleep
import telebot as tb
from config import *
from text_response import handle_response


@bot.message_handler(commands=['start'])
def start_bot(msg):
    try:
        bot.send_message(msg.chat.id, 'bot is ready')
    except Exception:
        print(traceback.format_exc())


@bot.message_handler(content_types=['text'])
def respond_to_msg(msg):
    try:
        handle_response(msg)
    except Exception:
        print(traceback.format_exc())


def main_polling_loop():
    while True:
        try:
            bot.polling()
        except tb.apihelper:
            print(traceback.format_exc())
            sleep(3)


if __name__ == '__main__':
    main_polling_loop()