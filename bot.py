#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from database.models import Song,Chat,Tracker,Player,Response

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    update.message.reply_text('Well met! I am MemeBot. '
                              'I respond to certain triggers with memes or songs, '
                              'and you can also approach me for hugs if you\'re '
                              'feeling lonely! \n\n'
                              'What are my triggers, you ask? Well, you\'ll have '
                              'to figure it out for yourself. ;) \n\n'
                              '/help for a list of my commands')


def help(bot, update):
    update.message.reply_text('WIP \n\n You don\'t get help. '
                              'Just like Harvey victims.')

def song(text,chat):
    s = Song.is_song(text)

    if s not None:
        c = Chat.get_chat(chat)
        t = Tracker.find_tracker(c,s)

        return t.next_line(text)

    return s

def meme(message_text):
    return Response.is_meme(message_text)

def respond(bot, update):
    res = None
    text = update.message.text
    chat = update.message.chat

    res = meme(text)
    if res not None:
        update.message.reply_text(res)
        return

    res = song(text,chat)
    if res not None:
        update.message.reply_text(res)
        return

    update.message.reply_text(res)


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    updater = Updater("443743656:AAH-NUwl0gDj-0W8hYMaUQUc5IcEuh-wOOU")
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(MessageHandler(Filters.text,
                                  respond,
                                  pass_chat_data = True))

    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
