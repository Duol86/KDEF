#version 2.0 of KDEF, now using the pycord API wrapper

#importing func.py, which contains database functions
import func
#<import discord> is importing package py-cord, which uses the same namespace as discord.py
import discord, sqlite3, random
from discord.ext import commands

c = sqlite3.connect("kygish.db")
cu = c.cursor()

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(
    command_prefix = [
        'ktest',
        'Ktest',
        'kt.'
        'Kt.'
    ],
intents=intents)

#Current guilds that the bot can use slash commands in
#Change to global later (?)
guilds = [939710720227041290]

@client.event
async def on_ready():
    print('running')

#slash command for adding a word to the database, responds with confirmation
@client.slash_command(guild_ids=guilds, description='Adds a new word and definition')
async def add(ctx, word, definition):
    #formatting
    word = word.capitalize()
    definition = definition.capitalize()

    func.add(word, definition)
    await ctx.respond(f'Added word `{word}` with definition `{definition}`')

#slash command to check the database for the defintion and respond with the opposite language's definition for the word
@client.slash_command(guild_ids=guilds, description='Searches for matching word')
async def define(ctx, word):
    #formatting
    word = word.capitalize()
    deff = func.keydef(word)

    try:
        await ctx.respond(f'{deff[2].capitalize()} definition: {deff[0]}')
    except:
        await ctx.respond(f'Word `{word}` not found, try checking spelling or adding the word yourself using `/add <word>`')

#deletes word from database, responds to message with confirmation
@client.slash_command(guild_ids=guilds, description='Deletes a word and definition')
async def delete(ctx, word):
    #formatting
    word = word.capitalize()

    if func.indb(word) == True:
        func.delete(word)
        await ctx.respond(f'Deleted word {word} and its definition')
    else:
        await ctx.respond(f'Word `{word}` not found, try checking spelling or adding the word yourself using `/add <word>`')

client.run('<token>')