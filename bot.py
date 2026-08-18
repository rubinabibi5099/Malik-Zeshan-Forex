import logging
import asyncio
from telegram.ext import ApplicationBuilder

# Aapka Bot Token
TOKEN = '8893964428:AAgcj_a0IYd59_XrBfQfSI3KfRQGMuabK_Y'
# Aapka Channel Username
CHANNEL_USERNAME = '@malikzeshanforexsignal'

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

async def send_test_message(context):
    message = (
        "🚀 **BOT TESTING LIVE!** 🚀\n\n"
        "✅ Bot successfully connected!\n"
        "⏱️ Interval: 5 Seconds\n"
        "📈 Status: Monitoring Mode Active\n\n"
        "*Yeh message har 5 second baad test ke liye bheja ja raha hai.*"
    )
    await context.bot.send_message(chat_id=CHANNEL_USERNAME, text=message, parse_mode='Markdown')

async def main():
    application = ApplicationBuilder().token(TOKEN).build()
    job_queue = application.job_queue
    
    # 5 second ka interval set kiya hai
    job_queue.run_repeating(send_test_message, interval=5, first=1)
    
    print("Bot is running... Testing messages started!")
    await application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
