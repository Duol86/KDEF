import sqlite3

con = sqlite3.connect('kygish.db')

con.execute('''CREATE TABLE kdef
("english" varchar,
"kygish" varchar)''')
con.commit()