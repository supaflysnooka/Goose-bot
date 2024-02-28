import os
import logging
import json
from twitchio.ext import commands
from twitchio import Message
from twitchio.ext import commands
from data_operations import load_data, save_data

# Import command modules
from cmd_coinflip import cmd_coinflip, prepare as prepare_coinflip
from cmd_commands import cmd_commands, prepare as prepare_commands
from cmd_compliment import cmd_compliment, prepare as prepare_compliment
from cmd_help import cmd_help, prepare as prepare_help
from cmd_insult import cmd_insult, prepare as prepare_insult
from cmd_lurk import cmd_lurk, prepare as prepare_lurk
from cmd_music import cmd_music, prepare as prepare_music
from cmd_musicsearch import cmd_musicsearch, prepare as prepare_musicsearch
from cmd_roll import cmd_roll, prepare as prepare_roll
from cmd_rules import cmd_rules, prepare as prepare_rules
from cmd_trust import cmd_trust, prepare as prepare_trust
# from cmd_urban import cmd_urban, prepare as prepare_urban


# Set logging level to DEBUG
logging.basicConfig(level=logging.DEBUG)
logging.getLogger('twitchio').setLevel(logging.WARNING)
# unhash below for additional debug messages
# print("TMI_TOKEN:", os.environ['TMI_TOKEN'])

bot_username = 'your_bot_username'
oauth_token = 'your_oauth_token'

bot = commands.Bot(
   # set up the bot
   token=os.environ['TMI_TOKEN'],
   client_id=os.environ['CLIENT_ID'],
   nick=os.environ['BOT_NICK'],
   prefix=os.environ['BOT_PREFIX'],
   initial_channels=[os.environ['CHANNEL']]
)

# Additional debugging print statements
print("Bot instance created. Connecting...")
# Call the prepare function for each command to add them to the bot
prepare_coinflip(bot)
prepare_commands(bot)
prepare_compliment(bot)
prepare_help(bot)
prepare_insult(bot)
prepare_lurk(bot)
prepare_music(bot)
prepare_musicsearch(bot)
prepare_roll(bot)
prepare_rules(bot)
prepare_trust(bot)
# prepare_urban(bot)

@bot.event
async def event_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"Sorry, {ctx.author.name}, I don't recognize that command. Type !help to see the available commands.")


if __name__ == "__main__":
    try:
        bot.run()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        logging.info("Bot execution completed.")