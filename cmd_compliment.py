# !compliment # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import random
from twitchio.ext import commands
from data_operations import load_data, save_data

@commands.command(name='compliment')
async def cmd_compliment(ctx, *args, compliments_file_path='C:\\Users\\neeee\\Documents\\Python\\goosetavobot\\compliments.json', trusted_users_data=None):
    if trusted_users_data is None:
        trusted_users_file_path = 'C:\\Users\\neeee\\Documents\\Python\\goosetavobot\\trusted_users.json'
        trusted_users_data = load_data(trusted_users_file_path)

    if args:
        # Check if the user invoking the command is in the trusted users list
        if ctx.author.name.lower() not in [user["username"].lower() for user in trusted_users_data]:
            # Check if the command is not "!compliment add"
            if args[0].lower() != 'add':
                # Return the argument and choose a random compliment without the user's name
                target_user = '@neeeekolaz' if args[0] == '@' else args[0]
                argument = ' '.join(args[1:]) if args[0] == '@' else ' '.join(args)
                compliment_entry = random.choice(load_data(compliments_file_path))
                await ctx.send(f"{target_user}, {compliment_entry['message']} (compliment #{compliment_entry['number']} by {compliment_entry['username']})")
            else:
                await ctx.send("Sorry, only trusted chatters can add compliments.")
        else:
            if args[0].lower() == 'add':
                if len(args) > 1:
                    new_compliment = ' '.join(args[1:])
                    # Get the current number of compliments and increment it
                    current_compliments = load_data(compliments_file_path)
                    current_number = len(current_compliments) + 1

                    compliment_entry = {"username": ctx.author.name, "message": new_compliment, "number": current_number}
                    await save_data(compliments_file_path, compliment_entry)
                    await ctx.send(f"compliment {current_number} added.")

                    # Reload compliments data after a new entry is added.
                    compliments_data = load_data(compliments_file_path)
                else:
                    await ctx.send("Please provide an compliment to add.")
            else:
                # Return the argument and choose a random compliment without the user's name
                target_user = '@neeeekolaz' if args[0] == '@' else args[0]
                argument = ' '.join(args[1:]) if args[0] == '@' else ' '.join(args)
                compliment_entry = random.choice(load_data(compliments_file_path))
                await ctx.send(f"{target_user}, {compliment_entry['message']} (compliment #{compliment_entry['number']} by {compliment_entry['username']})")
    else:
        # Choose a random compliment from the loaded compliments and include @neeeekolaz at the beginning
        compliment_entry = random.choice(load_data(compliments_file_path))
        await ctx.send(f"@neeeekolaz, {compliment_entry['message']} (compliment #{compliment_entry['number']} by {compliment_entry['username']})")

def prepare(bot):
    bot.add_command(cmd_compliment)
