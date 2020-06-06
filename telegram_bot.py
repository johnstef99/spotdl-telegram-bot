from telegram.ext import Updater, CallbackContext, CommandHandler
from telegram import Bot, Update
import sys
from spotdl.command_line.__main__ import main
import time

bot = Bot(token='ADD YOUR TOKEN HERE')

updater = Updater(bot=bot, use_context=True)

dispatcher = updater.dispatcher


def song(update: Update, context: CallbackContext):
    song = update.effective_message.text[6:]
    if(len(song) == 0):
        context.bot.send_message(
            chat_id=update.effective_chat.id, text='send the name or the spotify link of the song')
        return
    print('song: '+song)
    sys.argv = ['', '-s', song, '--overwrite', 'force']
    main(update, context)


def playlistToList(update: Update, context: CallbackContext):
    playlist = update.effective_message.text[15:]
    if(len(playlist) == 0):
        context.bot.send_message(
            chat_id=update.effective_chat.id, text='send the link of the spotify playlist')
        return
    print('playlist: ' + playlist)
    sys.argv = ['', '-p', playlist, '--overwrite', 'force']
    main(update, context)


def list_file(update: Update, context: CallbackContext):
    list_file = update.effective_message.text[6:]
    if(len(list_file) == 0):
        context.bot.send_message(
            chat_id=update.effective_chat.id, text='send the file.txt that you created from playlist2list')
        return
    print('listfile: '+list_file)
    sys.argv = ['', '-l', list_file, '--overwrite', 'force']
    main(update, context)


song_handler = CommandHandler('song', song)
dispatcher.add_handler(song_handler)

playlist_handler = CommandHandler('playlist2list', playlistToList)
dispatcher.add_handler(playlist_handler)

list_handler = CommandHandler('list', list_file)
dispatcher.add_handler(list_handler)

updater.start_polling()
