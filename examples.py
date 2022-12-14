import os
from bots.TelegramBot import TelegramBot
from bots.WhatsAppBot import WhatsAppBot


# -- Telegram Bot Example -- #
# Follow these links to get a token and chat-id
# - https://www.christian-luetgens.de/homematic/telegram/botfather/Chat-Bot.htm
# - https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id
token = '123456789:jbd78sadvbdy63d37gda37bd8'   # <-- Just a random example, replace with your Bot Token
chat_id = '1234567890'                          # <-- Just a random example, replace with your Chat ID
try:
    TBot = TelegramBot(chat_id, token)
    msg = 'Example script to send a message from the Telegram Bot :)'
    TBot.send_msg(msg)
except:
  print("An Unexpected Error when using Telegram Bot!")


# -- WhatsApp Bot Example -- #
# For first time use, the script will open up https://web.whatsapp.com/ and the site will require you to connect your phone with the web client by scanning a barcode through the WhatsApp app.
group_id = 'genjvsvdkngsejtgirsbnjkszf'       # <-- Just a random example, replace with your Group ID
try:
    WhatsBot = WhatsAppBot(group_id)
    msg = 'Example script to send a message from the WhatsApp Bot :)'
    WhatsBot.send_msg(msg)
    # Delete PyWhatKit_DB.txt for privacy issues
    curr_dir = os.path.abspath(__file__)
    pewhatkit_db = os.path.join(os.sep, *curr_dir.split(os.sep)[:-1], 'PyWhatKit_DB.txt')
    os.remove(pewhatkit_db)
except:
    print("An Unexpected Error when using WhatsApp Bot!")