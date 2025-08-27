import sqlite3

def add_book(title, author, year):
    conn=sqlite3.connect("books.db")
    cursor=conn.cursor()
    cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
                   (title, author, year))
    
    conn.commit()
    conn.close()

def view_books():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    conn.close()
    return rows

# update
def update_books(book_id, title, author, year):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET title=?, author=?, year=? where id=?",
                   (title, author, year, 1))
    conn.commit()
    conn.close()

def delete_book(book_id):
    conn=sqlite3.connect("books.db")
    cursor=conn.cursor()
    cursor.execute("DELETE FROM books WHERE id=?",(book_id,))
    conn.commit()
    conn.close()

# add_book("love is in the air", "Unknown", 2025)
# print(view_books())
# update_books(1, "dark", "xyz", 2021)
delete_book(3)
delete_book(4)
delete_book(5)
delete_book(6)
print(view_books())