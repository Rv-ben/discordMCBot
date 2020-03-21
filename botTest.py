import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'MC')


@client.command()
async def test(ctx):
    await ctx.send('This is a test')

client.run('')