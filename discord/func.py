import sqlite3

c = sqlite3.connect('kygish.db')

def add(e, k):
    c.execute(f'''INSERT INTO kdef(english, kygish)
    VALUES("{e}", "{k}")
    ''')
    c.commit()

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
        return [o, olang, olang2]

def indb(k):
    o = False
    cu = c.execute('SELECT * FROM kdef')
    for a in cu:
        if a[0] == k or a[1] == k:
            o = True
    return o

def delete(k):
    lang = keydef(k)[1]
    c.execute(f'DELETE FROM kdef WHERE {lang} = "{k}"')