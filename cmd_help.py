# !HELP # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
from twitchio.ext import commands

@commands.command(name='help')
async def cmd_help(ctx, *args):
    if not args:
        command_list = ", ".join([command.name for command in ctx.bot.commands.values() if isinstance(command, commands.Command)])
        await ctx.send(f"Use \"!help <command>\" for more specific help information. Available commands: {command_list} ")
    else:
        command_name = args[0]
        command = ctx.bot.get_command(command_name)
        if command and isinstance(command, commands.Command):
            if command.name == 'coinflip':
                await ctx.send(f"Displays a 50/50 heads or tails result. Also triggered by \"!coin\"")

            elif command.name == 'commands':
                await ctx.send(f"Lists all available commands for @goosetavobot.")

            elif command.name == 'compliment':
                await ctx.send(f"Sends a compliment to Neek, or add an @<user> to compliment them instead! Add compliments with \"!complement add <info>\"")
            
            elif command.name == 'help':
                await ctx.send(f"Use the !help command to get more information about a command. For example: \"!help help\"... wait a moment.")
            
            elif command.name == 'insult':
                await ctx.send(f"Sends an insult to Neek, or add an @<user> to insult them instead! Add insults with \"!insult add <info>\"")
            
            elif command.name == 'music':
                await ctx.send(f"The !music command will hotswap in-game music. Accepted input: \"!music <your search here>\". Add \"shuffle\" to the end to make music positions randomized. Try !musicsearch (or !ms) to see what is available.")
            
            elif command.name == 'musicsearch':
                await ctx.send(f"Usage: \"!musicsearch <your search terms here>\". Returns 10 results for your search term. If no search term is provided it will pull 10 random results. Also triggered by \"!ms <your search term here>\"")
            
            elif command.name == 'roll':
                await ctx.send(f"Usage: \"!roll <odds>\". Defaults to a d20.")
            
            elif command.name == 'rules':
                await ctx.send(f"Lists the rules")
            
            elif command.name == 'trust':
                await ctx.send(f"Usage: \"!trust <@user>\". Allows @'d person to add data to other commands.")
            else:
                pass
        else:
            print(f"Debug: Command name: {command_name}, Command: {command}, Type: {type(command)}")   
            await ctx.send(f"Command !{command_name} not found. Use !help to see all available commands.")

def prepare(bot):
    bot.add_command(cmd_help)