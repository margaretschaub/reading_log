import sqlite3
conn = sqlite3.connect('reading_log_database.db')
cur = conn.cursor()


s = "select id, title from books where author is null"
res = cur.execute(s)
for book_row in res.fetchall():
    print(f"the book '{book_row[1]}' has no author!")
    name = input("Please enter author name in format last name, first name: ")
    name = name.replace(" ","")
    book_title = book_row[1]
    last, first = name.split(",")
    a = f"INSERT OR IGNORE INTO authors (last_name, first_name) VALUES('{last}','{first}')"
    u = f'select id from authors where last_name = "{last}" and first_name = "{first}" COLLATE NOCASE'
    cur.execute(a)
    res2 = cur.execute(u)
    auth_id = res2.fetchone()
    print(f"author id is {auth_id[0]}")
    u2 = f"update books set author = {auth_id[0]} where title = '{book_title}'"
    res3 = cur.execute(u2)
    conn.commit()



