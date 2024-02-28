# cmd_lurk.py

from twitchio.ext import commands

@commands.command(name='lurk')
async def cmd_lurk(ctx):
    user_mention = ctx.author.display_name
    await ctx.send(f"{user_mention} is now lurking! Enjoy the stream!")

def prepare(bot):
    bot.add_command(cmd_lurk)
