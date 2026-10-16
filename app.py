import os
import requests
from flask import Flask

app = Flask(__name__)

# إعدادات تليجرام (استبدل القيم بمعلوماتك أو اتركها إذا كانت مضبوطة مسبقاً)
TOKEN = os.environ.get("TELEGRAM_TOKEN", "YOUR_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "YOUR_CHAT_ID")

def send_telegram_signal(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=payload)
        return response.json()
    except Exception as e:
        return str(e)

@app.route('/')
def home():
    # عند زيارة رابط موقعك على Netlify، سيقوم البوت بفحص السوق وإرسال الإشارة فوراً!
    # يمكنك وضع كود الاستراتيجية أو التحليل الخاص بك هنا
    signal_message = "🤖 *Binary Trading Bot:* تم فحص السوق بنجاح، البوت يعمل الآن عبر السحابة وجاهز لإرسال الإشارات!"
    result = send_telegram_signal(signal_message)
    return f"Bot executed successfully! Response: {result}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
