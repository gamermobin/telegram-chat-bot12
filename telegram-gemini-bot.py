import google.generativeai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# --- تنظیم API ها ---
TELEGRAM_TOKEN = "8126930463:AAFC_RZZIRrutpqVY_8o9E0qvwaaBC2u-YE"
GEMINI_API_KEY = "AIzaSyBQhSmCbsEhatk0dgyT6Xlkh-cOUxiaESo"

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

# --- پاسخ‌دهی به پیام‌ها ---
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    response = model.generate_content(user_text)
    await update.message.reply_text(response.text)

# --- شروع کار ربات ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! من یه چت‌بات هوش مصنوعی هستم. هر چی خواستی بپرس 🙂")

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("ربات روشن شد ✅")
    app.run_polling()

if __name__ == "__main__":
    main()