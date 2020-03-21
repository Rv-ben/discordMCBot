import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'MC')


@client.command()
async def test(ctx):
    await ctx.send('This is a test')

@client.command()
async def setIp(ctx,arg):
    await ctx.send(arg)

@client.event
async def on_message(msg):
    if(msg.author == discord.User.bot ):
        return
    
    #True if messages sender has admin permissions
    isAdmin = msg.author.guild_permissions.administrator

    message = msg.content

    isIp = message.startswith('MCIP')
    isPass = message.startswith('MCPASS')

    if(isAdmin):
        if(isIp):
            serverIp = message.strip('MCIP')
            await msg.channel.send('Server IP = '+serverIp)

        if(isPass):
            rconPass = message.strip('MCPASS')
            await msg.channel.send('RCON pass = '+ rconPass)

            
        

client.run('')