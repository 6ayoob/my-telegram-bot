import logging
import pandas as pd
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# إعداد التسجيل
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# أدخل توكن البوت من BotFather هنا
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# السماح فقط لحساب محدد باستخدام البوت
ALLOWED_USERNAME = 'tayoob07_bot'

# دالة وهمية لإرجاع بيانات الأسهم
def get_stock_movers():
    data = {
        'Symbol': ['AAPL', 'TSLA', 'AMZN'],
        'Price': [150.25, 720.12, 3345.55],
        'Change': [1.5, -2.3, 0.8]
    }
    df = pd.DataFrame(data)
    return df

# أوامر البوت
def start(update: Update, context: CallbackContext):
    if update.effective_user.username != ALLOWED_USERNAME:
        update.message.reply_text("🚫 غير مصرح لك باستخدام هذا البوت.")
        return
    update.message.reply_text('مرحباً! أرسل /movers للحصول على تحركات السوق.')

def movers(update: Update, context: CallbackContext):
    if update.effective_user.username != ALLOWED_USERNAME:
        update.message.reply_text("🚫 غير مصرح لك باستخدام هذا البوت.")
        return
    df = get_stock_movers()
    message = "📈 تحركات السوق:

"
    for _, row in df.iterrows():
        message += f"{row['Symbol']}: ${row['Price']} ({row['Change']}%)\n"
    update.message.reply_text(message)

# تشغيل البوت
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("movers", movers))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
