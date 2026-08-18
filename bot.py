import requests

# BotFather se liya gaya latest token
TOKEN = '8893964428:AAGcj_a0IYd59_XrBfQfSI3KfRQGMuabK_Y'
CHANNEL_USERNAME = '@malikzeshanforexsignal'

def send_signal():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    
    # Malik Zeshan Forex Signal Template
    message = (
        "👑 **MALIK ZESHAN FOREX SIGNAL** 👑\n\n"
        "📈 **Pair:** EURUSD\n"
        "📊 **Action:** BUY\n"
        "🕒 **Timeframe:** 1 Minute (Candle Close Entry)\n\n"
        "✅ _Bot successfully tested and connected via GitHub Actions!_"
    )
    
    payload = {
        "chat_id": CHANNEL_USERNAME,
        "text": message,
        "parse_mode": "Markdown"
    }
    
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Success: Signal sent to channel perfectly!")
    else:
        print(f"Failed: {response.status_code} - {response.text}")

if __name__ == "__main__":
    send_signal()
