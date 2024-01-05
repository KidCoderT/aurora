import os
import discord
from 
from dotenv import load_dotenv

load_dotenv()

class NeuralNexus(discord.Bot):
    async def on_ready(self):
        print(f"{self.user} is ready and online!")

