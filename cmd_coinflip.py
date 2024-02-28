# !COINFLIP # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import random
from twitchio.ext import commands

@commands.command(name='coinflip', aliases=['coin'])
async def cmd_coinflip(ctx):
    result = random.choice(['Heads', 'Tails'])
    await ctx.send(f"{result}")

def prepare(bot):
    bot.add_command(cmd_coinflip)