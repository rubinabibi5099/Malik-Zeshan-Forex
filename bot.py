import logging
import asyncio
from telegram.ext import ApplicationBuilder

# Aapka Bot Token aur Channel Username
TOKEN = '8893964428:AAgcj_a0IYd59_XrBfQfSI3KfRQGMuabK_Y'
CHANNEL_USERNAME = '@malikzeshanforexsignal'

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

async def send_test_message(context):
    try:
        message = (
            "🚀 **MALIK ZESHAN FOREX - TESTING LIVE!** 🚀\n\n"
            "✅ Bot successfully connected!\n"
            "⏱️ Interval: 5 Seconds\n"
            "📈 Status: Monitoring Mode Active\n\n"
            "_Yeh message testing ke liye bheja ja raha hai._"
        )
        await context.bot.send_message(chat_id=CHANNEL_USERNAME, text=message, parse_mode='Markdown')
        print("Test message sent successfully!")
    except Exception as e:
        print(f"Error sending message: {e}")

async def main():
    application = ApplicationBuilder().token(TOKEN).build()
    job_queue = application.job_queue
    
    # Har 5 second baad message bhejne ka job set kiya hai
    job_queue.run_repeating(send_test_message, interval=5, first=1)
    
    print("Bot is running... Testing messages started!")
    await application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
