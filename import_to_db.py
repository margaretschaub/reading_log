from main import *

author_list = parse_file("/Users/margaretschaub/Desktop/books_authors.txt")

import sqlite3
conn = sqlite3.connect('reading_log_database.db')
cur = conn.cursor()
cur.executemany("INSERT INTO authors(last_name, first_name) VALUES(?,?);", author_list)
conn.commit()

book_list = parse_file("/Users/margaretschaub/Desktop/books_table.txt")

convert_integers(book_list,2)
convert_integers(book_list,3)

from date_practice import convert_time
convert_time(book_list,4)

for each in book_list:
    del each[0]


final_list =(create_list_of_tuples(book_list))

cur.executemany("INSERT INTO books(title, isbn, page_count, publication_date) VALUES(?,?,?,?);", final_list)
conn.commit()

