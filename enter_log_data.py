import sqlite3
from datetime import datetime

conn = sqlite3.connect('reading_log_database.db')
cur = conn.cursor()

def convert_date(date):
    try:
        date_time_str = datetime.strptime(date, "%m/%d/%Y")
        new_format = date_time_str.strftime("%Y-%m-%d")
        return new_format
    except ValueError:
        try:
            date_time_str = datetime.strptime(date, "%m/%d/%y")
            new_format = date_time_str.strftime("%Y-%m-%d")
            return new_format
        except ValueError:
            print(f"Date entry error")

def make_int(value):
    new_value = int(value)
    return new_value

def make_float(value):
    new_value_2 =float(value)
    return new_value_2


print("This is a reading log!")
book = input("Please enter the name of the book: ")
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

b = f"SELECT id from books WHERE title = '{book}'"
res2 = cur.execute(b)
book_id = res2.fetchone()
a = f"INSERT OR IGNORE INTO log (started_date, finished_date, my_rating, library_book, format, purchased, book) VALUES('{started_date_clean}','{finished_date_clean}',{my_rating_clean},{library_book_clean},{format__clean},{purchased_clean},'{book_id[0]}')"
res1 = cur.execute(a)
conn.commit()
