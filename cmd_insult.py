# !INSULT # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import random
from twitchio.ext import commands
from data_operations import load_data, save_data

@commands.command(name='insult')
async def cmd_insult(ctx, *args, insults_file_path='C:\\Users\\neeee\\Documents\\Python\\goosetavobot\\insults.json', trusted_users_data=None):
    if trusted_users_data is None:
        trusted_users_file_path = 'C:\\Users\\neeee\\Documents\\Python\\goosetavobot\\trusted_users.json'
        trusted_users_data = load_data(trusted_users_file_path)

    if args:
        # Check if the user invoking the command is in the trusted users list
        if ctx.author.name.lower() not in [user["username"].lower() for user in trusted_users_data]:
            # Check if the command is not "!insult add"
            if args[0].lower() != 'add':
                # Return the argument and choose a random insult without the user's name
                target_user = '@neeeekolaz' if args[0] == '@' else args[0]
                argument = ' '.join(args[1:]) if args[0] == '@' else ' '.join(args)
                insult_entry = random.choice(load_data(insults_file_path))
                await ctx.send(f"{target_user}, {insult_entry['message']} (insult #{insult_entry['number']} by {insult_entry['username']})")
            else:
                await ctx.send("Sorry, only trusted chatters can add insults.")
        else:
            if args[0].lower() == 'add':
                if len(args) > 1:
                    new_insult = ' '.join(args[1:])
                    # Get the current number of insults and increment it
                    current_insults = load_data(insults_file_path)
                    current_number = len(current_insults) + 1

                    insult_entry = {"username": ctx.author.name, "message": new_insult, "number": current_number}
                    await save_data(insults_file_path, insult_entry)
                    await ctx.send(f"insult {current_number} added.")

                    # Reload insults data after a new entry is added.
                    insults_data = load_data(insults_file_path)
                else:
                    await ctx.send("Please provide an insult to add.")
            else:
                # Return the argument and choose a random insult without the user's name
                target_user = '@neeeekolaz' if args[0] == '@' else args[0]
                argument = ' '.join(args[1:]) if args[0] == '@' else ' '.join(args)
                insult_entry = random.choice(load_data(insults_file_path))
                await ctx.send(f"{target_user}, {insult_entry['message']} (insult #{insult_entry['number']} by {insult_entry['username']})")
    else:
        # Choose a random insult from the loaded insults and include @neeeekolaz at the beginning
        insult_entry = random.choice(load_data(insults_file_path))
        await ctx.send(f"@neeeekolaz, {insult_entry['message']} (insult #{insult_entry['number']} by {insult_entry['username']})")

def prepare(bot):
    bot.add_command(cmd_insult)
