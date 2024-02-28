import random
from twitchio.ext import commands

@commands.command(name='roll')
async def cmd_roll(ctx, arg: str): 
    # Default to d20 if no value is provided
    max_value = 20

    # Check if the input starts with "d" or "1" (optional) and extract the number
    if arg[0] == 'd':
        arg = arg[1:]
    elif arg[0] == '1':
        arg = arg[1:]

    try:
        max_value = int(arg)
    except ValueError:
        await ctx.send("Invalid input. Please use the format '!roll d20' or '!roll 20'.")
        return

    # Set an upper limit for the maximum value
    max_limit = 999

    if max_value <= 0:
        await ctx.send("How do I roll a die with negative numbers on it?")
        return
    elif max_value > max_limit:
        await ctx.send(f"The highest die I have is a D{max_limit}.")
        return

    result = random.randint(1, max_value)
    await ctx.send(f"{ctx.author.mention} rolled a d{max_value} and got {result}.")

# Prepare function to add the command to the bot
def prepare(bot):
    bot.add_command(cmd_roll)
