from parse_files import *
import sqlite3
from date_practice import convert_time

conn = sqlite3.connect('reading_log_database.db')
cur = conn.cursor()

book_list = parse_file("/Users/margaretschaub/Desktop/books_table.txt")

convert_integers(book_list,2)
convert_integers(book_list,3)

convert_time(book_list,4)

for each in book_list:
    del each[0]


final_list =(create_list_of_tuples(book_list))

cur.executemany("INSERT INTO books(title, isbn, page_count, publication_date) VALUES(?,?,?,?);", final_list)
# conn.commit()




