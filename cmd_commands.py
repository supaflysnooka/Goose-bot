from twitchio.ext import commands

@commands.command(name='commands', aliases=['cmds'])
async def cmd_commands(ctx):
    command_list = ", ".join([command.name for command in ctx.bot.commands.values() if isinstance(command, commands.Command)])
    await ctx.send(f"Available commands: {command_list}. Use !help for more information about these commands. \"!help <command>\".")

# Prepare function to add the command to the bot
def prepare(bot):
    bot.add_command(cmd_commands)