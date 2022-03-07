import logging
import os

from spotdl import Spotdl, util
from spotdl.command_line.core import Spotdl
from spotdl.helpers.spotify import SpotifyHelpers
from telegram import *
from telegram.ext import *

util.install_logger(logging.INFO)
old_fact = util.logging.getLogRecordFactory()


def song(update: Update, context: CallbackContext):

    def sendSong(filename):
        audio_file = open(filename, 'rb')
        context.bot.send_audio(
            chat_id=update.effective_chat.id, audio=audio_file)
        os.remove(filename)

    def sendMsg(message):
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=message)

    def record_factory(*args, **kwargs):
        record = old_fact(*args, **kwargs)
        if(record.levelname == "INFO"):
            sendMsg(record.msg)
        return record

    logging.setLogRecordFactory(record_factory)
    song = update.effective_message.text[6:]
    if(len(song) == 0):
        sendMsg('send the name or the link of the song')
        return
    print('/song: '+song)
    sendMsg("Search match for " + song)
    args = {
        "overwrite": "force"
    }
    with Spotdl(args) as spotdl_handler:
        filename = spotdl_handler.download_track(song)
        if(filename != "None"):
            sendSong(filename)


def main():
    bot = Bot(token=os.environ['BOT_TOKEN'])
    updater = Updater(bot=bot, use_context=True)
    dispatcher = updater.dispatcher
    song_handler = CommandHandler('song', song)
    dispatcher.add_handler(song_handler)

    updater.start_polling()


if __name__ == "__main__":
    main()
