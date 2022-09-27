#version 2.0 of KDEF, now using the pycord API wrapper and imroved DB

#importing func.py, which contains database functions
from operator import index
import func
#<import discord> is importing package py-cord, which uses the same namespace as discord.py
import discord, sqlite3, atexit, asyncio, hjson #json module can be imported instead, using file 'grammar.json'
from discord.ext import commands
from os import system
from sys import argv
from simple_chalk import green, red #for console display in verbose mode

try:
    if argv[1] == '-v':
        v = True
except IndexError:
    v = False

c = sqlite3.connect("kygish.db")
with open('grammar.hjson') as grammar:
    g = hjson.load(grammar)

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(
    command_prefix = [
        '__add__ ' #used only for adding a new guild
    ],

#REQUIRES MESSAGE CONTENT INTENTS
    intents=intents)

#Current guilds that the bot can use slash commands in
#Change to global later (?)

#assigning list 'guilds' to given command line arguments + default guilds
guilds = argv
try:
    if guilds[1] == '-v':
        guilds.pop(1)
except IndexError:
    pass
guilds.pop(0)

guilds.append(939710720227041290)
guilds.append(690194500039082053) #default guilds
for a in guilds:
    a = int(a)

print('Current guilds: {}'.format(guilds))

@client.event
async def on_ready():
    print('running')

#slash command for adding a word to the database, responds with confirmation
@client.slash_command(description='Adds a new word and definition')
async def add(ctx, word, definition):
    #formatting
    word = word.capitalize()
    definition = definition.capitalize()

    if func.indb != True:
        func.add(word, definition)
        await ctx.respond(f'Added word `{word}` with definition `{definition}`')
        if v == True:
            print(green(f'[{ctx.author.name}][add][{word}][{definition}]'))
    else:
        await ctx.respond(f'Word `{word}` already exists in KDEF')
        if v == True:
            print(red(f'[{ctx.author.name}][add][{word}][{definition}][return:__False__]'))

@client.slash_command(description='Shows the total amount of words in KDEF')
async def sum(ctx):
    await ctx.respond(f'There are {func.sum()} words stored in KDEF currently')

#slash command to check the database for the defintion and respond with the opposite language's definition for the word
@client.slash_command(description='Searches for matching word')
async def define(ctx, word):
    #formatting
    word = word.capitalize()
    deff = func.keydef(word)
    #deff = [word, word's language, definition's language]

    try:
        await ctx.respond(embed=discord.Embed(
            title = f'KDEF: {word}',
            description = f'{deff[2].capitalize()} definition: {deff[0]}',
            #description = 'english/kygish definition: word'
            color = discord.Color.purple()
        ))
    except:
        await ctx.respond(f'Word `{word}` not found, try checking spelling or adding the word yourself using `/add <word>`')
    if v == True:
        try:
            print(green(f'[{ctx.author.name}][define][{word}][return:{deff[0]}]'))
        except TypeError:
            print(red(f'[{ctx.author.name}][define][{word}][return:__False__]'))

@client.slash_command(description='Defines a word from a non-Kygish language')
async def extdefine(ctx, word, language):
    word = word.capitalize()
    language = language.lower()
    try:
        deff = func.extdefine(word, language)
    except:
        deff = False
    try:
        await ctx.respond(embed=discord.Embed(
            title = f'KDEF: {word}',
            description = deff[0],
            #description = 'english/kygish definition: word'
            color = discord.Color.purple()
        ))
    except:
        await ctx.respond(f'Word `{word}` not found, try checking spelling or adding the word yourself using `/add <word> <definition>`')
    if v == True:
        try:
            print(green(f'[{ctx.author.name}][define][{word}][return:\n{deff[0]}]'))
        except TypeError:
            print(red(f'[{ctx.author.name}][define][{word}][return:__False__]'))

@client.slash_command(description='Deletes a word from an external language')
@commands.has_permissions(manage_messages=True)
async def extdelete(ctx, word, language):
    word = word.capitalize()
    language = language.lower()
    dd = func.extindb(word, language)
    eidb = dd[0]
    if eidb == 0:
        await ctx.respond(f'Word `{word}` not found in KDEF')
        if v == True:
            print(red(f'[{ctx.author.name}][extdelete][{word}][{language}][return:__False__]'))
    elif eidb == 1:
        await func.deleteext(language, word)
        if v == True:
            print(green(f'[{ctx.author.name}][extdelete][{word}][{language}]'))
    else:
        string = ''
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        for a in range(0, len(dd[1])):
            string += f'[{a+1}] {dd[1][a][0]} = {dd[1][a][1]}\n'
        await ctx.respond(f"There are multiple definitions for word `{word}` in KDEF, please specify which one from this list you would like to delete:\n```{string}```")
        try:
            msg = await client.wait_for('message', check=check, timeout=10)
            msg = msg.content
        except asyncio.TimeoutError:
            await ctx.respond('Timed out')
            if v == True:
                print(red(f'[{ctx.author.name}][extdelete][{word}][{language}][return:__False__]'))
        try:
            msg = int(msg)-1
            func.extdeletemulti(language, dd[1][msg][0], dd[1][msg][1])
            await ctx.send(f'Word `{word}` and its definition deleted')
            if v == True:
                print(green(f'[{ctx.author.name}][extdelete][{word}][{language}][return:__True__]'))
        except:
            await ctx.send('An error occured, please try again, if this error persists, please contact the bot owner')
        

@client.slash_command(description='Adds a table to database')
async def addexttable(ctx, table):
    table = table.lower()
    func.addexttable(table)
    await ctx.respond(f'Added table `{table}` to db')
    if v == True:
        print(green(f'[{ctx.author.name}][addexttable][{table}]'))

@client.slash_command(description='Adds a word to an external table')
async def addext(ctx, language, word, definition):
    language = language.lower()
    word = word.capitalize()
    definition = definition.capitalize()
    try:
        func.addext(language, word, definition)
        await ctx.respond(f'Added word `{word}` with definition `{definition}` to language `{language}`')
    except:
        await ctx.respond(f'Language `{language}` not found, please add it using `/addexttable <table>`')

#deletes word from database, responds to message with confirmation
@client.slash_command(description='Deletes a word and definition')
async def delete(ctx, word):
    #formatting
    word = word.capitalize()

    if func.indb(word) == True:
        func.delete(word)
        await ctx.respond(f'Deleted word {word} and its definition')
        if v == True:
            print(green(f'[{ctx.author.name}][delete][{word}]'))
    else:
        await ctx.respond(f'Word `{word}` not found, try checking spelling or adding the word yourself using `/add <word>`')
        if v == True:
            print(red(f'[{ctx.author.name}][delete][return:False]'))

@client.slash_command(description='Grammar guide for Kygish')
async def grammar(ctx, page):
    try:
        await ctx.respond(embed=discord.Embed(
            title='Grammar',
            description=g[page],
            colour=discord.Color.purple()
        ))
        if v == True:
            print(green(f'[{ctx.author.name}][grammar][{page}]'))
    except:
        await ctx.respond(f'Error: Page `{page}` is not valid')
        if v == True:
            print(red(f'[{ctx.author.name}][grammar][{page}][return:False]'))

def exitHandling():
    system('cp -r kygish.db ~ && cp -r ext.db ~')
    print('\n\n    Copied kygish.db and ext.db to home directory   \n\n')
atexit.register(exitHandling)

#note to self: remember to hide token when uploading to github
client.run('token')
