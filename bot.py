#Configuración del bot de discord
import discord
from Clase3_bot_logic import gen_pass, gen_emodji, flip_coin
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    #Pude corregir el error de que el bot repitiera el mensaje
    if message.author == client.user:
        return
    if message.content.startswith('$hola'):
        await message.channel.send("Hola, Daniel")
    elif message.content.startswith('$adiós'):
        await message.channel.send("Hasta luego\U0001f642")
    elif message.content.startswith("password"):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith("emoji"):
        await message.channel.send(gen_emodji())
    elif message.content.startswith("moneda"):
        await message.channel.send(flip_coin())

client.run("MTMwMjA3NDk5NTUxMzYyNjY0NA.Go_RA3.BuWsviIBfnFOqIF-hDvXl22UdP5R2ZDGrfTfZk")
