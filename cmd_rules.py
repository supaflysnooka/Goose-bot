# cmd_rules.py

from twitchio.ext import commands

@commands.command(name='rules', aliases=['rule'])
async def cmd_rules(ctx):
    rules_list = [
        "1) Don't be an asshole. ",
        "2) Be respectful of everyone here. ",
        "3) No harrassing/bullying/hate speech/deragatory language. ",
        "Failure to adhere will result in a ban from the channel."
    ]
    await ctx.send("\n".join(rules_list))

def prepare(bot):
    bot.add_command(cmd_rules)
