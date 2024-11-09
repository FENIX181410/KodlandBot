import discord
from discord.ext import commands
from bot_logic import gen_pass, gen_emoji, flip_coin

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send(f'Hola,{client.user} soy el bot {bot.user}!')

@bot.command()
async def contraseña(ctx, x):
    await ctx.send(gen_pass(x))

@bot.command()
async def emoji(ctx):
    await ctx.send(gen_emoji())

@bot.command()
async def moneda(ctx):
    await ctx.send(flip_coin())

bot.run("TOKEN AQUÍ")
