import sqlite3

def test_insert_user():
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)")
    cursor.execute("DELETE FROM users")
    cursor.execute("INSERT INTO users (id, name) VALUES (?, ?)", (1, "Frances"))
    conn.commit()

    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    assert result == [(1, "Frances")]

    conn.close()