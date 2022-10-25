file1 = open("/Users/margaretschaub/Desktop/books_table.txt","r")

books = file1.readlines()

book_list = []
for each in books:
    new = each.replace(" ","")
    new_2 = new.split(",")
    book_list.append(new_2)


# n=0

# for each in book_list:
#     try:
#         book_list[n][0] = int(book_list[n][0])
#         book_list[n][2] = int(book_list[n][2])
#         book_list[n][3] = int(book_list[n][3])
#     except(ValueError):
#         print(f"Entry error at {book_list[n][1]}")
#     n += 1

def convert_integers(name_of_list,index_value):
    n=0
    for each in name_of_list:
        try:
            name_of_list[n][index_value] = int(name_of_list[n][index_value])
        except(ValueError):
            print(f"Entry error at {name_of_list[n][1]}")
    n += 1

convert_integers(book_list,0)
convert_integers(book_list,2)
convert_integers(book_list,3)


# def import_and_make_lists(file_entry):
#     book_list = []
#     books = file_entry.readlines()
#     for each in books:
#         new = each.replace(" ", "")
#         new_2 = new.split(",")
#         book_list.append(new_2)
#     return book_list
#
# print(import_and_make_lists(file1))