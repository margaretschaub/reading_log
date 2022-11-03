from main import *
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


# author_list = create_list_of_tuples(parse_file("/Users/margaretschaub/Desktop/books_authors.txt"))
#
# cur.executemany("INSERT INTO authors(last_name, first_name) VALUES(?,?);", author_list)
# # conn.commit()
#
# author_key = [6, 2, 3, 4, 5, 1, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 14, 23, 24,
# 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 30, 39, 40, 41, 42, 43, 44,
# 45, 46, 47, 48, 49, 1, 50, 51, 52, 53, 57, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63,
# 64, 25, 24]


