import discord
from discord.ext import commands
from bot_logic import gen_pass, gen_emoji, flip_coin, juego

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='K!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send(f'Hola, {ctx.author.name} soy el bot {bot.user}!')

@bot.command()
async def contraseña(ctx, x):
    await ctx.send(gen_pass(x))

@bot.command()
async def emoji(ctx):
    await ctx.send(gen_emoji())

@bot.command()
async def moneda(ctx):
    await ctx.send(flip_coin())
    
@bot.command()
async def juego(ctx):
    await ctx.send(juego())

bot.run("TOKEN AQUÍ")
