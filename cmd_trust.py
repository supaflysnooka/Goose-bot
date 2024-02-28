# !TRUST # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
from twitchio.ext import commands
from data_operations import load_data, save_data

# Import trusted users data
trusted_users_file_path = 'C:\\Users\\neeee\\Documents\\Python\\goosetavobot\\trusted_users.json'
global trusted_users_data
trusted_users_data = load_data(trusted_users_file_path)

@commands.command(name='trust')
async def cmd_trust(ctx, target_user: str):
    global trusted_users_data

    # Check if the user invoking the command is the bot owner (replace 'owner_username' with your username)
    if ctx.author.name.lower() != 'neeeekolaz':
        return await ctx.send("You are not authorized to use this command.")

    # Check if a target user is provided
    if not target_user:
        return await ctx.send("Please provide a user to trust.")

    # Remove @ before saving
    target_user = target_user.lstrip('@')

    # Process trust
    trusted_user_entry = {"username": target_user.lower()}  # lowercase for consistency

    # Check if the user is already trusted
    existing_usernames = [user["username"] for user in trusted_users_data]
    if target_user.lower() in existing_usernames:
        return await ctx.send(f"{target_user} is already trusted.")

    # Save trusted user
    await save_data(trusted_users_file_path, trusted_user_entry)
    await ctx.send(f"{target_user} is now trusted.")

    # Reload trusted users data after a new entry is added.
    trusted_users_data = load_data(trusted_users_file_path)
    print(f"Updated trusted_users_data: {trusted_users_data}")

# Prepare function to add the command to the bot
def prepare(bot):
    bot.add_command(cmd_trust)
