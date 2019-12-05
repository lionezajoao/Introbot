import discord
import asyncio
import random
import introbot

client = discord.Client()

status = "bot online porra"
path = "/home/d4rthbodus/Repositorios/introbot-420/"

#vendo os status do bot no terminal
@client.event
async def on_ready():
    print(status.upper())


#interação com o bot
@client.event
async def on_message(message):
    if message.content.lower().startswith('!koe'):
        await message.channel.send("qq vc quer porra")

#---------------------------------------------------------------------#
    
    if message.content.lower().startswith("!moeda"):
        choice = random.randint(1,2)
        if choice == 1:
            await message.channel.send("Cara, seu animal")
        else:
            await message.channel.send("Coroa, burro")

#---------------------------------------------------------------------#

    if message.content.lower().startswith("!name"):
        nome = message.content.replace("!name ", '')
        if nome == "!name":
            await message.channel.send("`Escreva um nome após '!name'`")
        else:
            await message.channel.send("`Bem vindx, "+nome+", ainda não entendo sua utilidade aqui.`")
    
#---------------------------------------------------------------------#
#Gerar a mensagem, id e registro:

    if message.content.lower().startswith("!generate"):
        msg = introbot.gerar(path)
        await message.channel.send(msg)

#---------------------------------------------------------------------#
#Recebendo a id e gerando novamente a mensagem

    if message.content.lower().startswith("!retrieve"):
        idaux = message.content.replace("!retrieve ", '')
        idaux = idaux.replace(",", '')
        if idaux == "!retrieve":
            await message.channel.send("`Escreva o ID gerado junto com '!retrieve'`")
        else:
            idaux.replace("!retrive ", '')
            await message.channel.send(introbot.recriar(path, idaux))

#---------------------------------------------------------------------#
#Mensagem de ajuda

    if message.content.lower().startswith("!help"):
        await message.channel.send("**"+"```!generate = Gera a mensagem de boas-vindas.\n\n!retrieve <id> = usando o ID gerado, recria a mensagem de boas vindas.\n\n"+"-"*20+"\n\nComandos secundários:\n\n!name <Nome> = uma linda mensagem.\n\n!moeda = Cara ou Coroa educado.\n\n\n\nEsse bot possui um easter egg, ache-o.```"+"**")
#token do bot       

client.run("TOKEN")