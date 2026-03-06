from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# ⚠️ Remplace par ton token du bot
TOKEN = "8733681410:AAEWP-K8AkHtH2HA6C9AvpJtAJe00HSI9DU"

# ⚠️ Remplace par ton user_id Telegram (trouvé via @userinfobot)
MY_USER_ID = 8598044133

# Handler pour recevoir les commandes depuis la mini-app
async def recevoir_commande(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.message.web_app_data.data
    # envoyer directement la commande sur ton compte perso
    await context.bot.send_message(
        chat_id="@leplug330bdx",
        text=f"Nouvelle commande Jackal : {data}"
    )
    # optionnel : confirmer à l'utilisateur
    await update.message.reply_text("Merci, votre commande a été reçue !")

# Initialisation du bot
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, recevoir_commande))
app.run_polling()
