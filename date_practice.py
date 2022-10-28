# from datetime import datetime
#
# now = "8/13/19"
#
# date_time_str = datetime.strptime(now,"%m/%d/%Y")
#
# new_format = date_time_str.strftime("%Y-%m-%d")
#
# print(new_format)

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

cat = parse_file("/Users/margaretschaub/Desktop/books_table.txt")

def convert_time(name_of_list, index_value):
    from datetime import datetime
    n = 0
    for each in name_of_list:
        try:
            now = name_of_list[n][index_value]
            date_time_str = datetime.strptime(now, "%m/%d/%Y")
            new_format = date_time_str.strftime("%Y-%m-%d")
            name_of_list[n][index_value] = new_format
        except ValueError:
            try:
                now = name_of_list[n][index_value]
                date_time_str = datetime.strptime(now, "%m/%d/%y")
                new_format = date_time_str.strftime("%Y-%m-%d")
                name_of_list[n][index_value] = new_format
            except ValueError:
                print(f"Entry error at {name_of_list[n][1]}")
                pass

        n += 1
