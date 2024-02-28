# cmd_urban.py

import requests
from twitchio.ext import commands

async def send_message(ctx, message):
    # Check if the message length exceeds Twitch's limit
    max_length = 500
    if len(message) <= max_length:
        await ctx.send(message)
    else:
        # Split the message into smaller chunks
        message_chunks = [message[i:i+max_length] for i in range(0, len(message), max_length)]
        for chunk in message_chunks:
            await ctx.send(chunk)

@commands.command(name='urban')
async def cmd_urban(ctx):
    # Get the query after !urban
    query = ctx.message.content[len('!urban'):].strip()

    if not query:
        await ctx.send("Please provide a word or phrase to look up on Urban Dictionary.")
        return

    # Fetch data from Urban Dictionary API
    url = f'https://api.urbandictionary.com/v0/define?term={query}'
    response = requests.get(url)
    data = response.json()

    if 'list' in data and data['list']:
        # Find the entry with the highest number of upvotes
        best_entry = max(data['list'], key=lambda entry: entry['thumbs_up'])

        # Get the best definition and number of upvotes
        best_definition = best_entry['definition']
        upvotes = best_entry['thumbs_up']

        # Construct the message
        message = f"Urban Dictionary defintion of '{query}': {best_definition}"

        # Send the message
        await send_message(ctx, message)
    else:
        await ctx.send(f"No definition found for '{query}' on Urban Dictionary.")

def prepare(bot):
    bot.add_command(cmd_urban)
