import sqlite3

conn = sqlite3.connect('reading_log_database.db')
cur = conn.cursor()

s = "select id_number, title from books where author is null limit 1"
res = cur.execute(s)
for book_row in res.fetchall():
    print(f"the book '{book_row[1]}' has no author!")
    name = input("author name")
    first, last = name.split(",", 1)
    u = f'select id_number from authors where last_name = "{last}" and first_name = "{first}" limit 1'
    res2 = cur.execute(u)
    auth_id = res2.fetchone()
    print(f"author id is {auth_id[0]}")
    u2 = f"update books set author = {auth_id[0]} where id_number = {book_row[0]}"
    res3 = cur.execute(u2)


# conn.commit()

