import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
TELEGRAM_TOKEN = 7876577316:AAGKni4m9_jKjXCDC_tkfvaIejkCcQnav4w
GROUP_CHAT_ID = -1002453436740  
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
def start(update: Update, context: CallbackContext):
    update.message.reply_text('سلام! اسم آهنگ رو بفرست تا برات دانلود کنم 🎵')
def search_and_send(update: Update, context: CallbackContext):
    song_name = update.message.text
    youtube_search_url = f"https://www.youtube.com/results?search_query={song_name.replace(' ', '+')}"
    soundcloud_search_url = f"https://soundcloud.com/search?q={song_name.replace(' ', '%20')}"
    spotify_search_url = f"https://open.spotify.com/search/{song_name.replace(' ', '%20')}"
    best_link = youtube_search_url  
    context.bot.send_message(chat_id=GROUP_CHAT_ID, text=best_link)
    update.message.reply_text(f"🎵 جستجو انجام شد! \n📌 یوتیوب: {youtube_search_url} \n📌 ساندکلاد: {soundcloud_search_url} \n📌 اسپاتیفای: {spotify_search_url} \n\n لطفا صبر کن تا دانلود انجام شود... ⏳")
def forward_file(update: Update, context: CallbackContext):
    if update.message.chat_id == GROUP_CHAT_ID:  # بررسی اینکه پیام از گروه خصوصی آمده است
        if update.message.video or update.message.audio or update.message.document:
            # ارسال فایل برای کاربری که درخواست داده بود
            update.message.forward(chat_id=update.message.reply_to_message.chat_id)
def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, search_and_send))
    dp.add_handler(MessageHandler(Filters.video | Filters.audio | Filters.document, forward_file))
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()