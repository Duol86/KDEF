import sqlite3

c = sqlite3.connect('kygish.db')

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

#Checks database for whether or not the word exists, returns True or False
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