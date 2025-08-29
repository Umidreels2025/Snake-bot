import os
from telebot import TeleBot, types

BOT_TOKEN = os.environ.get("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN topilmadi. Render Environment Variables bo‘limida qo‘shganingni tekshir.")

bot = TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("O‘ynash 🎮", callback_game=types.CallbackGame())
    markup.add(btn)
    bot.send_game(message.chat.id, "ilon", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.game_short_name == "ilon":
        bot.answer_callback_query(call.id, url="https://umidjon.github.io/Snake-game/")

print("✅ Bot ishga tushdi...")
bot.polling(non_stop=True)
