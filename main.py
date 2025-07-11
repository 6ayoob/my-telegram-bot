import logging
import pandas as pd
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# إعدادات السجل
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# المتغيرات البيئية (ستتم قراءتها من Render)
import os
TOKEN = os.getenv('BOT_TOKEN')
ALLOWED_USERNAME = os.getenv('tayoob07')

# دالة وهمية لتحركات السوق
def get_stock_movers():
    data = {
        'Symbol': ['AAPL', 'TSLA', 'AMZN'],
        'Price': [150.25, 720.12, 3345.55],
        'Change': [1.5, -2.3, 0.8]
    }
    return pd.DataFrame(data)

def start(update: Update, context: CallbackContext):
    if update.effective_user.username != tayoob07:
        update.message.reply_text("🚫 غير مصرح لك باستخدام هذا البوت.")
        return
    update.message.reply_text('مرحباً! أرسل /movers للحصول على تحركات السوق.')

def movers(update: Update, context: CallbackContext):
    if update.effective_user.username != tayoob07:
        update.message.reply_text("🚫 غير مصرح لك باستخدام هذا البوت.")
        return
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
