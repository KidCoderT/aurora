import os
import discord
from dotenv import load_dotenv

load_dotenv()

bot = discord.Bot()


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.event
async def on_message(message: discord.Message):
    print("MESSAGE WAS SENT")


@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")


@bot.slash_command(name="stats", description="Bot Stats")
async def stats(ctx: discord.ApplicationContext):
    latency = round(bot.latency * 1000)
    await ctx.respond(f"bot: {bot.user}\nlatency: {latency}")


bot.run(os.getenv("DISCORD_TOKEN"))
