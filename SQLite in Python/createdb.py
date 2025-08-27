import sqlite3

conn = sqlite3.connect("books.db")
cursor = conn.cursor()

# Create Table 
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               title TEXT NOT NULL,
               author TEXT,
               year INTEGER
)
""")
conn.commit()
conn.close()