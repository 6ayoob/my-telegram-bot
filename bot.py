import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import pandas as pd

TOKEN = os.environ.get("BOT_TOKEN")

def get_stock_movers():
    data = {
        'Symbol': ['AAPL', 'TSLA', 'AMZN'],
        'Price': [150.25, 720.12, 3345.55],
        'Change': [1.5, -2.3, 0.8]
    }
    df = pd.DataFrame(data)
    return df

def start(update: Update, context: CallbackContext):
    update.message.reply_text('مرحباً! أرسل /movers للحصول على تحركات السوق.')

def movers(update: Update, context: CallbackContext):
    df = get_stock_movers()
    message = "📈 تحركات السوق:\n\n"
    for _, row in df.iterrows():
        message += f"{row['Symbol']}: ${row['Price']} ({row['Change']}%)\n"
    update.message.reply_text(message)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("movers", movers))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
