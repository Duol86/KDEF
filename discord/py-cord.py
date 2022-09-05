#token == MTAxNjEwMzc1ODc3MTUzOTk5OQ.G6Jkds.NUFdTdzKyQGb-k-7F-Qf-87G6cDbU4AHgjsjH4

#version 2.0 of KDEF, now using the pycord API wrapper

import func
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

guilds = [939710720227041290]

@client.event
async def on_ready():
    print('running')

@client.slash_command(guild_ids=guilds, description='Adds a new word and definition')
async def add(ctx, word, definition):
    word = word.capitalize()
    definition = definition.capitalize()
    func.add(word, definition)
    await ctx.respond(f'Added word `{word}` with definition `{definition}`')

@client.slash_command(guild_ids=guilds, description='Searches for matching word')
async def define(ctx, word):
    word = word.capitalize()
    deff = func.keydef(word)
    if deff[1] == 'kygish':
        await ctx.respond(f'english definition: {deff[0]}')
    elif deff[1] == 'english':
        await ctx.respond(f'kygish definition: {deff[0]}')

client.run('<token>')
