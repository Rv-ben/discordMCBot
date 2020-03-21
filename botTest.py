import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'MC')


@client.command()
async def setIp(ctx,arg):

    isAdmin = ctx.message.author.guild_permissions.administrator
    
    if(isAdmin):
        ip = arg
        await ctx.send(ip)
    else:
        await ctx.send('You are not admin')

@client.command()
async def setPass(ctx,arg):

    isAdmin = ctx.message.author.guild_permissions.administrator
    
    if(isAdmin):
        passWord = arg
        await ctx.send(passWord)
    else:
        await ctx.send('You are not admin')    

client.run('')