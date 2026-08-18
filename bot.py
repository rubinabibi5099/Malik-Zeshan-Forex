import time
import requests

# Aapka Bot Token aur Channel Username
TOKEN = '8893964428:AAgcj_a0IYd59_XrBfQfSI3KfRQGMuabK_Y'
CHANNEL_USERNAME = '@malikzeshanforexsignal'

def send_telegram_message():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_USERNAME,
        "text": "🚀 **MALIK ZESHAN FOREX - GITHUB TEST LIVE!** 🚀\n\n✅ Bot successfully triggered via GitHub Actions!\n📈 Status: Working perfectly.",
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Message sent successfully to channel!")
        else:
            print(f"Failed to send message: {response.text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Bot script started...")
    send_telegram_message()
    print("Execution finished.")
