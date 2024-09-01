import discord
from discord.ext import commands
import os
from dotenv_vault import load_dotenv

load_dotenv()

token = os.getenv('TOKEN')

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='-', intents=intents)

# class myClient(discord.Client):
#     async def on_ready(self):
#         print(f'Logged on as {self.user}')
        
#     async def on_message(self, message):
#         print(f'Message From ⤵ \n channel: {message.channel.name}\n name: {message.author}\n message: {message.content}')
    
        
# client = myClient(intents = intents)

@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')
    
@bot.event
async def on_message(message):
    if message.content.startswith('-') or message.author == bot.user:
        pass
    else:
        print(f'Message from {message.author}: {message.content}')
    
    await bot.process_commands(message)
    
    
# @bot.command()
# async def test(ctx, args):
#     await ctx.send(args)

# @bot.command()
# async def test(ctx, arg1, arg2):
#     await ctx.send(f'You passed {arg1} and {arg2}')

# @bot.command()
# async def test(ctx, *args): #for taking multiple parameter -> *args 
#     arguments = ', '.join(args)
#     await ctx.send(f'{len(args)} arguments: {arguments}')
    
@bot.command()
async def test(ctx, args1, *, args2):
    await ctx.send(f'{args1}\n{args2}')

# Invocation Context
@bot.command()
async def info(ctx, message):
    guild = ctx.guild
    msg = ctx.message
    author = ctx.author
    await ctx.send(f'{msg.author}')

# Converters

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)

def to_upper(argument):
    return argument.upper()

@bot.command()
async def up(ctx, *, content: to_upper):
    await ctx.send(content)
    
# discord converters

@bot.command()
async def joined(ctx, *, member: discord.Member):
    await ctx.send(f'{member} has joined at {member.joined_at}')

# discord attachments

@bot.command()
async def upload(ctx, attachment: discord.Attachment):
    await ctx.send(f'You have uploaded <{attachment.url}>')


bot.run(token)
# remove token first then push