import os
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler

TOKEN = os.getenv('BOT_TOKEN')
wishes_channel_id = os.getenv('CHANNEL_ID')

init_text = '''
Hola @{} bienvenido al bot de Deseos del
Canal Extra, deje su deseo y en
medida de las posibilidades
se subira al Canal.
'''


def start(update, context):
    username = update.effective_user.username
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=init_text.format(username)
    )


def wish_handler(update, context):
    message_id = update.effective_message.message_id
    from_id = update.effective_chat.id
    context.bot.copy_message(wishes_channel_id, from_id, message_id)


def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(filters=Filters.chat_type.private & Filters.text, callback=wish_handler))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
