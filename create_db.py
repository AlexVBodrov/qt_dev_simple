import sqlite3

# create connection to
conn = sqlite3.connect('users.db')

# create cursor for
cur = conn.cursor()

# create table
cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY,
   name TEXT,
   password TEXT);""")

# save to database
conn.commit()

# insert values into database
cur.execute("""INSERT INTO users(userid, name, password) 
   VALUES('00001', 'Alex', '1234');""")
cur.execute("""INSERT INTO users(userid, name, password) 
   VALUES('00002', 'Lena', '12345');""")

# save to database
conn.commit()