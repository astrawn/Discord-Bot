# Discord Bot
import discord
import random
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

TOKEN = null

client = discord.Client()

@ client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    # bot's responses to users
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)
    elif message.content.startswith('Thank you!'.lower()):
        msg = "You're welcome!".format(message)
        await message.channel.send(msg)
    elif message.content.startswith('!wiki'):
        try:
            query1 = message.content[6:-1]
            query = 'wikipedia ' + query1
            for j in search(query, tld = "com", num=1, stop=1, pause=2):
                msg = j.format(message)
                await message.channel.send(msg)
        except:
            msg = 'Search failed. Please contact an administrator to report this issue.'.format(message)
            await message.channel.send(msg)
    elif message.content.startswith('!def'):
        try:
            query1 = message.content[5:-1]
            query = query1 + ' definition'
            for j in search(query, tld = "com", num=1, stop=1, pause=2):
                msg = j.format(message)
                await message.channel.send(msg)
        except:
            msg = 'Search failed. Please contact an administrator to report this issue.'.format(message)
            await message.channel.send(msg)
    elif message.content.startswith('!rng'):
        msg = str(random.randint(1, 101)).format(message)
        await message.channel.send(msg)
    elif message.content.startswith('!bot'):
        msg = 'I am a bot!'.format(message)
        await message.channel.send(msg)
    elif message.content.startswith('bot!'):
        num = random.randint(1, 101)
        if num > 85:
            msg = 'WHAT??!'.format(message)
            await message.channel.send(msg)
        elif num < 85 and num > 75:
            msg = 'yes?'.format(message)
            await message.channel.send(msg)
        elif num < 75 and num > 55:
            msg = 'BOT!'.format(message)
            await message.channel.send(msg)
        elif num < 55 and num > 45:
            msg = 'Hello!'.format(message)
            await message.channel.send(msg)
        else:
            msg = '{0.author.mention}!'.format(message)
            await message.channel.send(msg)
    elif 'bot' in message.content:
        msg = 'Did someone call me?'.format(message)
        await message.channel.send(msg)
    elif message.content.startswith('!div'):
        list = message.content.split(' ')
        try:
            num1 = int(list[1])
            num2 = int(list[2])
            num3 = num1 / num2
            msg = str(num3).format(message)
            await message.channel.send(msg)
        except:
            msg = "I'm sorry, but I can't do that.".format(message)
            await message.channel.send(msg)
    elif message.content.startswith('!mul'):
        list = message.content.split(' ')
        try:
            num1 = int(list[1])
            num2 = int(list[2])
            num3 = num1 * num2
            msg = str(num3).format(message)
            await message.channel.send(msg)
        except:
            msg = 'Error!'.format(message)
            await message.channel.send(msg)
    elif message.content.startswith('!add'):
        list = message.content.split(' ')
        try:
            num1 = int(list[1])
            num2 = int(list[2])
            num3 = num1 + num2
            msg = str(num3).format(message)
            await message.channel.send(msg)
        except:
            msg = 'Cannot calculate this value.'.format(message)
            await message.channel.send(msg)
    elif message.content.startswith('!sub'):
        list = message.content.split(' ')
        try:
            num1 = int(list[1])
            num2 = int(list[2])
            num3 = num1 - num2
            msg = str(num3).format(message)
            await message.channel.send(msg)
        except:
            msg = 'Not a number!'.format(message)
            await message.channel.send(msg)

@ client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
