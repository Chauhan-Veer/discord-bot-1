import os
#from dotenv import load_dotenv

import discord
from discord.ext import commands

#load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.listen()
async def on_ready():
    print('Bot loaded and ready!')

@bot.command(name="hi", help="Says hello")
async def say_hello(ctx):
    await ctx.send(f"Hello {ctx.author.display_name}")

    
# kick member
#use !kich @username
@bot.command()
async def kick( ctx, user: discord.Member,*, reason=None):
    if ctx.author.guild_permissions.administrator:
        await user.kick(reason=reason)
        embed = discord.Embed(title = "KICK",description = f"{user.mention} has been removed")
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title = "KICK", description=f" {ctx.author.mention} you don't have permissions to use this command" )
        await ctx.send(embed=embed)

    
    
    
bot.run(TOKEN)


