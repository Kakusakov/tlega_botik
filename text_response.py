from config import bot


def msgdata(msg):
    bot.send_message(msg.chat.id, msg)


def ping(msg):
    bot.send_message(msg.chat.id, 'pong')


resps = {
    'msgdata': msgdata,
    'ping': ping
}


def default_resp(msg):
    bot.send_message(msg.chat.id, "sorry, I can\'t understand this command yet!")


def handle_response(msg):
    for command, commandResp in resps.items():
        if msg.text.lower() == command:
            return commandResp(msg)
    return default_resp(msg)
