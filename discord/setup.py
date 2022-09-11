import sqlite3
from os import system

try:
    import py-cord
except:
    print('installing dependency py-cord\n\n\n')
    system('python -m pip install discord')
    print('\n\n\ninstalled dependency discord')

try:
    import hjson
except:
    print('installing dependency hjson\n\n\n')
    system('python -m pip install hjson')
    print('\n\n\ninstalled dependency hjson')

try:
    con = sqlite3.connect('kygish.db')
    con.execute('SELECT * FROM kdef')
except:
    con = sqlite3.connect('kygish.db')

    con.execute('''CREATE TABLE kdef
    ("english" varchar,
    "kygish" varchar)''')
    con.commit()
