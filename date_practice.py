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
