import discord
from discord.ext import commands
from bot_logic2 import gen_pass, gen_emoji, flip_coin, juego
import os

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
async def contraseña(ctx, x:int):
    await ctx.send(gen_pass(x))

@bot.command()
async def emoji(ctx):
    await ctx.send(gen_emoji())

@bot.command()
async def moneda(ctx):
    await ctx.send(flip_coin())
    
juegos_activos = {}

@bot.command(name='jugar')
async def jugar(ctx):
    juegos_activos[ctx.author.id] = 1 
    await ctx.send("¡Juego iniciado! Cada uno empieza con una bala. Escribe 'recargar', 'disparar' o 'bloquear'.")
    
@bot.command(name='accion')
async def accion(ctx, eleccion: str):
    if ctx.author.id not in juegos_activos:
        await ctx.send("Primero debes iniciar el juego con el comando 'K!jugar'.")
        return
    
    resultado = juego(eleccion.lower())
    await ctx.send(resultado)
    
    if "ganado" in resultado or "terminado" in resultado:
        juegos_activos.pop(ctx.author.id)
        
@bot.command(name='terminar')
async def terminar(ctx):
    if ctx.author.id in juegos_activos:
        juegos_activos.pop(ctx.author.id)
        await ctx.send("El juego ha terminado.")
    else:
        await ctx.send("No tienes un juego en curso.")
        
@bot.command()
async def meme(ctx):
    Lista= os.listdir('Kodland/Clase 5/memes')
    for i in Lista:
        with open(f'Kodland/Clase 5/memes/{i}', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
            
@bot.command()
async def juegos(ctx):
    Lista= os.listdir('Kodland/Clase 5/juegos')
    for i in Lista:
        with open(f'Kodland/Clase 5/juegos/{i}', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)            
            
@bot.command()
async def música(ctx):
    Lista= os.listdir('Kodland/Clase 5/Artistas')
    for i in Lista:
        with open(f'Kodland/Clase 5/Artistas/{i}', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)                  


bot.run("TOKEN")
