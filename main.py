import os
import discord
from discord.ext import bridge
from dotenv import load_dotenv
from rich import print
from classes import ai

load_dotenv()

import database

bot_intent = discord.Intents.default()
bot_intent.message_content = True
bot_intent.messages = True
bot_intent.members = True

bot = discord.Bot(intents=bot_intent, owner_id=912949047650824282, commands_prefix="!")

ART = r"""
[bold blue]
   _____                                           
  /  _  \   __ __ _______   ____  _______ _____    
 /  /_\  \ |  |  \\_  __ \ /  _ \ \_  __ \\__  \   
/    |    \|  |  / |  | \/(  <_> ) |  | \/ / __ \_ 
\____|__  /|____/  |__|    \____/  |__|   (____  / 
        \/                                     \/  
[/bold blue]
> {} is active 🤘🤘!
 - Made By Tejas
"""


@bot.event
async def on_ready():
    print(ART.format(bot.user))


token = str(os.getenv("DISCORD_TOKEN"))

extensions = ["ai", "fun"]
bot.load_extensions(*[f"cogs.{extension}" for extension in extensions])

if __name__ == "__main__":
    database.create_tables()
    ai.setup_client()
    bot.run(token)
