import discord
from discord.ext import commands

client = commands.Bot(command_prefix="hello@")

@client.event
async def on_ready():
    print("hello is online")

@client.command()
async def halo(ctx):
    await ctx.send("halo halo halo")

client.run("token")