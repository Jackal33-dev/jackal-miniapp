from telegram.ext import MessageHandler, filters

async def web_app_data(update: Update, context: ContextTypes.DEFAULT_TYPE):

    data = update.message.web_app_data.data

    await update.message.reply_text(
        f"Commande reçue : {data}"
    )

app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, web_app_data))