import sqlite3
from enter_log_data import *

conn = sqlite3.connect('reading_log_database.db')
cur = conn.cursor()


def find_book():
    c = f"SELECT id, title from books;"
    res3 = cur.execute(c)
    for each in res3.fetchall():
        print(each)
    selection = input("Please select id that matches book you choose: ")
    print(f"The id you selected is {selection}")
    return int(selection)


def master_import(table_name, dictionary):
    key = []
    value = []

    for each in dictionary.keys():
        v = dictionary[each]
        key.append(each)
        value.append(v)

    column_names = ",".join(key)

    a = f"INSERT OR IGNORE INTO {table_name} ({column_names}) VALUES({value})"
    res1 = cur.execute(a)


def create_dict_log(book_id):

    started_date = input("Please enter date you started reading in format m/d/Y: ")
    finished_date = input("Please enter date you finished reading in format m/d/Y: ")
    library_book= input("Was this book a library book? Please enter 1 if Yes, 0 if No ")
    format_ = input("Please enter 1 if you read this book as a physical copy, 2 if audiobook, 3 if virtual copy: ")
    purchased = input("Did you purchase this book? Please enter 1 if Yes, 0 if No. Audible books count as purchased.")
    my_rating = input("Please enter your rating: ")

    started_date_clean = convert_date(started_date)
    finished_date_clean = convert_date(finished_date)
    library_book_clean = make_int(library_book)
    format__clean = make_int(format_)
    purchased_clean = make_int(purchased)
    my_rating_clean = make_float(my_rating)

    dict_log = {"started_date": started_date_clean, "finished_date": finished_date_clean, "my_rating": my_rating_clean, "library_book": library_book_clean, "format": format__clean, "purchased": purchased_clean, "book": book_id}

    return dict_log


# dict_genre = {"book_id":"","genre":""}
# dict_authors ={"last_name":"","first_name":""}
# dict_books = {"title":"", "isbn":"", "page_count": "", "publication_date":"", "author":""}
# dict_to_read = {"date_added_TBR":"", "book_id":""}








