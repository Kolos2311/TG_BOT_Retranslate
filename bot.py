from telegram import Update, Bot
from telegram.ext import Updater, MessageHandler, Filters

bot = Bot(token='YOUR_BOT_TOKEN')

def forward_message(update: Update, context):
    if update.message:
        update.message.forward(chat_id='TARGET_CHAT_ID')

updater = Updater(token='YOUR_BOT_TOKEN')
updater.dispatcher.add_handler(MessageHandler(Filters.all, forward_message))
updater.start_polling()
