from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters
)

BOT_TOKEN = "8765370367:AAFdTWiXZgyXFrZ76WOUGJ5Htteskl4kWf8"

ADMIN_ID = 7490075648   # sizning Telegram ID


# /id (test uchun)
async def getid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"ID: {update.message.chat_id}")


# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("✉️ Admin ga xabar qoldirish", callback_data="support")]
    ]

    await update.message.reply_text(
        "👋 Xush kelibsiz!\n\nAgar admin javob bermasa, xabar qoldirishingiz mumkin.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# button bosilganda
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "support":
        context.user_data["waiting_message"] = True

        await query.message.reply_text(
            "✍️ Xabaringizni yozing va yuboring."
        )


# text kelganda
async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if context.user_data.get("waiting_message"):

        user = update.message.from_user
        message = update.message.text

        text = f"""
📩 Yangi xabar

👤 Ism: {user.first_name}
🆔 ID: {user.id}
💬 Username: @{user.username}

✉️ Xabar:
{message}
"""

        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=text
        )

        context.user_data["waiting_message"] = False

        await update.message.reply_text("✅ Xabaringiz yuborildi!")


# bot
app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("id", getid))
app.add_handler(CallbackQueryHandler(button_handler))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))

print("Bot ishladi...")
app.run_polling()