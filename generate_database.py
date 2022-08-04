import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute('''

create table posts(
id integer primary key autoincrement,
name text not null,
content text not null);
          ''')

conn.commit()
conn.close()