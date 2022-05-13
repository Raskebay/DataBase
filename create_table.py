import sqlite3
from logpass import x

base = sqlite3.connect('new.db')
cur = base.cursor()

base.execute('CREATE TABLE IF NOT EXISTS {}(login PRIMARY KEY, password)'.format('data'))
base.commit()
'''
cur.execute('INSERT INTO data VALUES(?, ?)', ('jonny23', '123456'))
base.commit()
cur.execute('INSERT INTO data VALUES(?, ?)', ('tony', '2674342'))
base.commit()

cur.executemany('INSERT INTO data VALUES(?, ?)', (x))
base.commit()
'''

d = cur.execute('SELECT* FROM data').fetchall()
l = cur.execute('SELECT login FROM data').fetchall()
print(d, l)

p = cur.execute('SELECT password FROM data WHERE login == ?', ('jonny23',)).fetchone()
print(p)

cur.execute('UPDATE data SET password == ? WHERE login == ?', ('parol', 'tony'))
base.commit()

cur.execute('DELETE FROM data WHERE login == ?', ('jonny23',))
base.commit()

base.execute('DROP TABLE IF EXISTS data')
base.commit()
base.close()
