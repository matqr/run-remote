import os
import time
import telegram
import credentials as cd

from telegram.error import NetworkError
from telegram.error import Unauthorized

"""
For instructions for how to create your bot, refer to https://core.telegram.org/bots
"""

def main():
    """Run the bot."""
    # Telegram Bot Authorization Token
    bot = telegram.Bot(cd.token)
    log_path = cd.repo + '/' + cd.log_file
    chat_id = cd.chat_id
    ending_phrase = cd.ending_phrase
    update_id = None
    
    # get the first pending update_id, this is so you can skip over
    # it in case it is an "Unauthorized" exception
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    while True:
        experiment_ended(bot, chat_id, log_path, ending_phrase)
        try:
            # send latest logs of running experiment
            update_id = reply(bot, chat_id, update_id, log_path)
        except NetworkError:
            time.sleep(1)
        except Unauthorized:
            update_id += 1

def reply(bot, chat_id, update_id, log_path):
    """Assumes you are the only one talking to this bot."""

    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1
        if 'logs' in update.message.text:
            message = check_logs(log_path) 
            update.message.reply_text(message)

    return update_id

def check_logs(log_path):
    try:
        stream = os.popen(f'tail -n 5 {log_path}')
        output = stream.read()
    except:
        output = 'Nothing Found'

    return output

def experiment_ended(bot, chat_id, log_path, ending_phrase):
    """Check if the experiment has ended and notify you when an experiment 
    has ended"""
    output = check_logs(log_path)

    if ending_phrase in output:
        # the experiment script finished
        send_message(bot, chat_id, output)
        
def send_message(bot, chat_id, message):
    bot.send_message(chat_id=chat_id, text=message)

if __name__ == '__main__':
    main()

