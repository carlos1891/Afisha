   ```python
   from telegram import Update
   from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

   # Función de inicio
   def start(update: Update, context: CallbackContext) -> None:
       update.message.reply_text('¡Hola! Soy tu bot.')

   # Función para manejar mensajes de texto
   def echo(update: Update, context: CallbackContext) -> None:
       update.message.reply_text(update.message.text)

   def main() -> None:
       # Reemplaza 'YOUR_TOKEN' con el token que te proporcionó BotFather
       updater = Updater("YOUR_TOKEN")

       # Obtiene el despachador para registrar los manejadores
       dispatcher = updater.dispatcher

       # Registra los manejadores
       dispatcher.add_handler(CommandHandler("start", start))
       dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

       # Comienza el bot
       updater.start_polling()

       # Corre el bot hasta que se detenga
       updater.idle()

   if __name__ == '__main__':
       main()
   ```

