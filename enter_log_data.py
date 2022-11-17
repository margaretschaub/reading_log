from datetime import datetime


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


