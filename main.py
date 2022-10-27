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
    for each in name_of_list:
        try:
            each[index_value] = int(each[index_value])
        except ValueError:
            print(f"Entry error at {each[1]}")


cat = parse_file("/Users/margaretschaub/Desktop/books_table.txt")

print(cat)
print(type(cat))

convert_integers(cat, 0)
convert_integers(cat, 2)
convert_integers(cat, 3)

print(parse_file("/Users/margaretschaub/Desktop/books_authors.txt"))

author_list = parse_file("/Users/margaretschaub/Desktop/books_authors.txt")

n=1
for item in author_list:
    item.insert(0, n)
    n += 1

print(author_list)