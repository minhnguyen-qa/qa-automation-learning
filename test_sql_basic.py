import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)")
conn.commit()
cursor.execute("DELETE FROM users")
cursor.execute("INSERT INTO users (id, name) VALUES (?, ?)", (1, "Frances"))
conn.commit()
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())
conn.close()