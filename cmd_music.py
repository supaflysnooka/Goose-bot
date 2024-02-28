# !MUSIC # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import random
import subprocess
import time
import asyncio
from fuzzywuzzy import process
from twitchio.ext import commands
from music_paths import script_paths


def fuzzy_search(query, keys, limit=5, threshold=80):
   matches = process.extract(query, keys, limit=limit)
   filtered_matches = [match[0] for match in matches if match[1] >= threshold]
   return filtered_matches
min_interval_seconds = 60
last_execution_times = 0

@commands.command(name='music')
async def cmd_music(ctx, *args):
    global last_execution_times

    def get_script_entry(search_args):
        # Makes search arguments look directly at 'keys'
        for entry in script_paths.values():
            keys = entry.get('keys', [])
            for key in keys:
                if search_args.lower() == key.lower():
                    return entry
        return None

    if args and args[0].lower() == 'list':
        # Provide a URL in the chat for the list
        music_list_url = "http://tinyurl.com/bdhtxuwm" 
        await ctx.send(f"Here's all the music available: {music_list_url}")
        return

    if args and args[0].lower() == 'reset':
        # names below can use this subcommand. (how tf do you restrict this by role?)
        if ctx.author.name.lower() in ['neeeekolaz', 'moderator2', 'moderator3']:
            last_execution_times = 0
            await ctx.send("!music is ready to be swapped.")
        else:
            await ctx.send("You don't have the required permissions to use this command.")
        return

    if 'search' in args:
        await ctx.send("Please try !musicsearch or !ms to do a search.")
        return

    if not args:
        await ctx.send("The !music command will hotswap in-game music. Accepted input: \"!music <your search here>\". Add \"shuffle\" to the end to make music positions randomized. Try !musicsearch (or !ms) to see what is available.")
        return

    shuffle_triggered = False

    if args[-1].lower() == 'shuffle':
        shuffle_triggered = True
        script_entry = get_script_entry(' '.join(args[:-1]))
    else:
        script_entry = get_script_entry(' '.join(args))

    if script_entry:
        comment = script_entry['comment']
        script_path = script_entry['path']

        current_time = time.time()
        time_difference = current_time - last_execution_times

        if time_difference < min_interval_seconds:
            await ctx.send(f"For better or for worse, we're listening to {comment} for at least one minute. In {int(min_interval_seconds - time_difference)} seconds the !music command will be ready, honk!")
            return

        last_execution_times = current_time

        if shuffle_triggered:
            await ctx.send(f"Now changing in-game to {comment} SHUFFLED. Any song from this music pack can be placed anywhere. Working...")
            subprocess.run(["python", script_path])
            await ctx.send("Done!")
        else:
            await ctx.send(f"Now swapping in-game music to {comment} Working...")
            subprocess.run(["python", script_path])

            with open(script_path, 'r', encoding='utf-8') as script_file:
                script_content = script_file.read()

            if 'Partial MSU' in script_content or 'Limited MSU' in script_content:
                await ctx.send(f"Done! FYI, this is a partial music pack; some music may not have changed!")
            else:
                await ctx.send(f"Done!")

            await asyncio.sleep(59)
            await ctx.send("!music swap is ready, honk!")

    else:
        if not shuffle_triggered:
            # If no exact match and shuffle not triggered, perform fuzzy search on the keys of all sections
            all_keys = [key.lower() for section in script_paths.values() for key in section.get('keys', []) if 'shuffle' not in key.lower() and 'random' not in key.lower() and ' - ' not in key.lower()]
            matches = fuzzy_search(' '.join(args), all_keys)

            if matches:
                # If fuzzy matches are found, provide all matches (not just a random sample)
                fuzzy_search_result_count = 5  # Change this number to the desired count
                await ctx.send(f"Did you mean one of these? {', '.join(matches[:fuzzy_search_result_count])}")
            else:
                # If no matches, provide random suggestions from all script paths
                fuzzy_search_result_count = 10  # Change this number to the desired count
                random_arguments = random.sample(list(script_paths.keys()), min(fuzzy_search_result_count, len(script_paths)))
                await ctx.send(f"Nothing found... Here's a few random suggestions: {', '.join(random_arguments)}")

def prepare(bot):
    bot.add_command(cmd_music)