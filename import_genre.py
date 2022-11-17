import sqlite3

conn = sqlite3.connect('reading_log_database.db')
cur = conn.cursor()

book = input("Please enter the name of the book: ")
book = book.strip()
genre = input("Please enter the genre for the book:")
genre = genre.lower()
genre_split = genre.split(",")


for each in genre_split:
    b = f"SELECT id from books WHERE title = '{book}'"
    res2 = cur.execute(b)
    book_id = res2.fetchone()
    a = f"INSERT OR IGNORE INTO genre (genre, book_id) VALUES('{each.strip()}',{book_id[0]})"
    res1 = cur.execute(a)
    conn.commit()

#error when entering only one (not a list)

