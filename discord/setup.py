import sqlite3
from os import system

try:
    import discord
except:
    print('installing dependency pycord\n\n\n')
    system('python -m pip install py-cord')
    print('\n\n\ninstalled dependency pycord')

try:
    import hjson
except:
    print('installing dependency hjson\n\n\n')
    system('python -m pip install hjson')
    print('\n\n\ninstalled dependency hjson')

try:
    import simple_chalk
except:
    print('installing dependency simple-chalk\n\n\n')
    system('python -m pip install simple-chalk')
    print('\n\n\ninstalled dependency simple-chalk')

try:
    con = sqlite3.connect('kygish.db')
    con.execute('SELECT * FROM kdef')
except:
    con = sqlite3.connect('kygish.db')

    con.execute('''CREATE TABLE kdef
    ("english" varchar,
    "kygish" varchar)''')
    con.commit()

try:
    con = sqlite3.connect('ext.db')
    con.execute('SELECT * FROM kazakan')
except:
    con = sqlite3.connect('ext.db')

    con.execute('''CREATE TABLE kazakan
    ("english" varchar,
    "kazakan" varchar)''')
    con.commit()
