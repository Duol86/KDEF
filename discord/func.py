import sqlite3

c, ex = sqlite3.connect('kygish.db'), sqlite3.connect('ext.db')

#Adds a new word to the database
def add(e, k):
    c.execute(f'''INSERT INTO kdef(english, kygish)
    VALUES("{e}", "{k}")
    ''')
    c.commit()

#Searches db for the word and its definition
def keydef(k):
    o = ''
    cu = c.execute('SELECT * FROM kdef')
    for a in cu:
        if k == a[0]:
            o = a[1]
            olang = 'english'
            olang2 = 'kygish'
        elif k == a [1]:
            o = a[0]
            olang = 'kygish'
            olang2 = 'english'
    if o == '':
        return False
    else:
        #returns [definition, word's language, definition's language]
        return [o, olang, olang2]

def extsum(lang):
    sums = ex.execute(f'SELECT * FROM {lang}')
    x = 0
    for a in sums:
        x += 1
    return x

def extdefine(k, lang):
    o = ''
    olen = 0
    cu = ex.execute(f'SELECT * FROM {lang} WHERE {lang} = "{k}"')
    co = ex.execute(f'SELECT * FROM {lang} WHERE english = "{k}"')
    for a in cu:
        o += f'(English) {a[0]}: {a[1]}\n'
        olen += 1
    for a in co:
        o += f'({lang.capitalize()}) {a[0]}: {a[1]}\n'
        olen += 1
    if o == '':
        return False
    else:
        return [o, olen]

def addexttable(table):
    ex.execute(f'''CREATE TABLE {table}(
        english text,
        {table} text
    )''')
    ex.commit()

def addext(table, e, k):
    ex.execute(f'''INSERT INTO {table}(english, {table})
    VALUES("{e}", "{k}")
    ''')
    ex.commit()


#Checks database for whether or not the word exists, returns True or False
def extindb(k, lang):
    o = False
    words = []
    cu = ex.execute(f'SELECT * FROM {lang}')
    for a in cu:
        if a[0] == k:
            o += 1
            words.append([a[1], k])
        elif a[1] == k:
            o += 1
            words.append([a[0], k])
    return [o, words]

def deleteext(table, k):
    ex.execute(f'DELETE FROM {table} WHERE english = "{k}" OR {table} = "{k}"')

def extsum(table):
    sums = ex.execute(f'SELECT * FROM {table}')
    x = 0
    for a in sums:
        x += 1
    return x

def extdeletemulti(table, k, e):
    ex.execute(f'DELETE FROM {table} WHERE (english = "{e}" AND {table} = "{k}") OR (english = "{k}" AND {table} = "{e}")')

def indb(k):
    o = False
    cu = c.execute('SELECT * FROM kdef')
    for a in cu:
        if a[0] == k or a[1] == k:
            o = True
    return o

#deletes a word from the database
def delete(k):
    lang = keydef(k)[1]
    c.execute(f'DELETE FROM kdef WHERE {lang} = "{k}"')

def sum():
    sums = c.execute(f'SELECT * FROM kdef')
    x = 0
    for a in sums:
        x += 1
    return x

#chooses a random word from the database
#def returnrand(k):
#    rand = c.execute(f'''SELECT kygish FROM kdef
#    ORDER BY random()
#    LIMIT 1;''')
#    rand2 = c.execute('''SELECT english FROM kdef
#    ORDER BY random()
#    LIMIT 1;''')
#    print(rand)