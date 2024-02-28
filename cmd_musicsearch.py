# !MUSICSEARCH # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
import random
from twitchio.ext import commands
from music_paths import script_paths
from fuzzywuzzy import process
def fuzzy_search(query, keys, limit=5, threshold=80):
   matches = process.extract(query, keys, limit=limit)
   filtered_matches = [match[0] for match in matches if match[1] >= threshold]
   return filtered_matches



@commands.command(name='musicsearch', aliases=['ms', 'search'])
async def cmd_musicsearch(ctx, *args):
    if not args:
        all_keys = [key for entry in script_paths.values() for key in entry.get('keys', []) if 'shuffle' not in key.lower() and 'random' not in key.lower() and ' - ' not in key.lower()]
        random_keys = [key for key in all_keys]
        selected_keys = random.sample(random_keys, min(15, len(random_keys)))
        await ctx.send(f"No search term or phrase provided. Here's a few random !music options: {', '.join(selected_keys)}")
    else:
        argument = ' '.join(args).lower()
        all_keys = [key.lower() for entry in script_paths.values() for key in entry.get('keys', []) if 'shuffle' not in key.lower() and 'random' not in key.lower() and ' - ' not in key.lower()]
        matches = fuzzy_search(argument, all_keys, limit=10)
        if matches:
            random_matches = random.sample(matches, min(10, len(matches)))
            await ctx.send(f"Search results: {', '.join(random_matches)}")
        else:
            random_arguments = random.sample(list(script_paths.keys()), min(5, len(script_paths)))
            await ctx.send(f"No results found for '{argument}'. Here's a few random suggestions: {', '.join(random_arguments)}")

def prepare(bot):
    bot.add_command(cmd_musicsearch)