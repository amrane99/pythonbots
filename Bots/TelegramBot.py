# ------------------------------------------------------------------------------
# Telegram bot to pass messages about the training, or inform when experiments 
# are done. Follow these links to get a token and chat-id
# - https://www.christian-luetgens.de/homematic/telegram/botfather/Chat-Bot.htm
# - https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id
# Then, place these strings in a telegram_login.json file in this directory. 
# That file is ignored by git.
# ------------------------------------------------------------------------------

import telegram as tel

class TelegramBot():
    r"""Initialize a telegram bot"""
    def __init__(self, chat_id, token):
        r"""Provide Bots chat id and token"""
        self.chat_id = chat_id
        self.bot = tel.Bot(token=token)

    def send_msg(self, msg):
        r"""Send a message in string form"""
        self.bot.send_message(chat_id=self.chat_id, text=msg)