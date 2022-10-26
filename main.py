#"/Users/margaretschaub/Desktop/books_table.txt"

def parse_file(file_location):

    book_list = []
    with open(file_location, "r") as f:
       lines = f.readlines()
       for line in lines:
            raw_column_values = line.split(",")
            # now we have the columns and can clean them up
            row_list = []
            for c in raw_column_values:
                row_list.append(c.strip())

            book_list.append(row_list)
    return book_list


def convert_integers(name_of_list, index_value):
    n = 0
    for each in name_of_list:
        try:
            name_of_list[n][index_value] = int(name_of_list[n][index_value])
        except ValueError:
            print(f"Entry error at {name_of_list[n][1]}")

        n += 1


cat = parse_file("/Users/margaretschaub/Desktop/books_table.txt")

print(cat)
print(type(cat))

convert_integers(cat, 0)
convert_integers(cat, 2)
convert_integers(cat, 3)
