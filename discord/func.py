import sqlite3

c = sqlite3.connect('kygish.db')

def add(e, k):
    c.execute(f'''INSERT INTO kdef(english, kygish)
    VALUES("{e}", "{k}")
    ''')
    c.commit()

def keydef(k):
    o = 0
    cu = c.execute('SELECT * FROM kdef')
    for a in cu:
        if k == a[0]:
            o = a[1]
            olang = 'english'
        elif k == a [1]:
            o = a[0]
            olang = 'kygish'
    if o == 0:
        return False
    else:
        return [o, olang]