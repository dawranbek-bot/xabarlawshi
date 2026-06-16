import telebot
import requests

TOKEN = "8874804432:AAFV_kKsEzX1xL6VQXfRlRDl3y93noRtxH4"
bot = telebot.TeleBot(TOKEN)
import telebot
import requests

TOKEN = "8874804432:AAFV_kKsEzX1xL6VQXfRlRDl3y93noRtxH4"
bot = telebot.TeleBot(TOKEN)

weather_codes = {
    0: "☀️ Quyoshli",
    1: "🌤 Qisman bulutli",
    2: "⛅ Bulutli",
    3: "☁️ Juda bulutli",
    61: "🌧 Yomg'irli",
    63: "🌧 Kuchli yomg'ir",
    71: "❄️ Qor",
    95: "⛈ Momaqaldiroq"
}

@bot.message_handler(commands=['obhavo'])
def weather(message):
    url = ("https://api.open-meteo.com/v1/forecast?"
           "latitude=42.95&longitude=59.82"
           "&current_weather=true")

    data = requests.get(url).json()

    temp = data["current_weather"]["temperature"]
    code = data["current_weather"]["weathercode"]

    holat = weather_codes.get(code, "🌍 Noma'lum")

    text = f"""
📍 Chimboy

🌡 Harorat: {temp}°C
🌤 Holat: {holat}
"""

    bot.send_message(message.chat.id, text)

bot.infinity_polling()
