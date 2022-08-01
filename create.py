import sqlite3
con = sqlite3.connect('opentutorials.db')
cur = con.cursor()
title = input('title? ')
body = input('body? ')
view = input('view? ')
result = cur.execute('INSERT INTO topics (title, body, created, view) VALUES(?, ?, DATE(), ?)',(title, body, view))
con.commit()

result = cur.execute('SELECT * FROM topics WHERE id = ?', (cur.lastrowid,))
rows = result.fetchone()
print(rows)
con.close()
