import sys
from datetime import datetime


known_genre = ["fiction", "action & adventure", "alternative history", "anthology", "asian american", "biography",
               "classic", "comics", "coming of age", "crime", "dystopian", "disaster", "fantasy", "folklore", "ghost",
               "gothic", "graphic novel", "hispanic & latino", "historical", "horror", "lgbtq+", "magical realism",
               "medical", "mystery", "cozy mystery", "mythology", "nature & the environment", "political",
               "psychological", "religious", "romance", "sagas", "satire", "science fiction", "short stories",
               "thrillers",
               "historical fiction", "autobiography", "nonfiction", "science", "women", "ya", "true crime"]


def clean_to_int(r):
    try:
        r = int(r)
        return r
    except ValueError:
        raise Exception(f"The value {r} is not valid.  it must be an int")


def clean_to_float(f):
    try:
        f = float(f)
        return f
    except ValueError:
        raise Exception(f"The value {f} is not valid.  it must be a float")


def clean(g):
    g = g.lower().strip()
    return g


def convert_date(d):
    try:
        date_time_str = datetime.strptime(d, "%m/%d/%Y")
        new_format = date_time_str.strftime("%Y-%m-%d")
        return new_format
    except ValueError:
        try:
            date_time_str = datetime.strptime(d, "%m/%d/%y")
            new_format = date_time_str.strftime("%Y-%m-%d")
            return new_format
        except ValueError:
            raise Exception(f"Date entry error {d} is not valid. m/d/y")


def author_last(a):
    last, first = a.split(",")
    last = last.strip()
    return last


def author_first(a):
    last, first = a.split(",")
    first = first.strip()
    return first


def clean_genre(x):
    x = x.lower().strip()
    x = x.replace(", ", ",")
    x = x.split(",")
    for each in x:
        if each.strip() not in known_genre:
            raise Exception(f"Genre not recognized at {each}")
        return x


def main():
    print(sys.argv)
    if sys.argv[1] == "add":
        try:
            title = sys.argv[2]
            isbn = clean_to_int(sys.argv[3])
            page_count = clean_to_int(sys.argv[4])
            publication_date = convert_date(sys.argv[5])
            last = author_last(sys.argv[6])
            first = author_first(sys.argv[6])
            genre = clean_genre(sys.argv[7])

            print(f"adding new book: title={title}, isbn={isbn}, page count={page_count}, "
                  f"publication date = {publication_date}, author last name = {last}, author first name = {first}",
                  f"genre = {genre}")
            return 0
        except IndexError:
            print("You did not pass the correct # of arguments. Please use command --help")

    if sys.argv[1] == "--help":
        print("You need help")

    elif sys.argv[1] == "done":
        try:
            title = sys.argv[2]
            started_date = convert_date(sys.argv[3])
            finished_date = convert_date(sys.argv[4])
            my_rating = clean_to_float(sys.argv[5])
            library_book = clean_to_int(sys.argv[6])
            format_book = clean_to_int(sys.argv[7])
            purchased = clean_to_int(sys.argv[8])

            print(f"adding to finished log: title={title}, started date={started_date}, finished date={finished_date}, "
                  f"my rating = {my_rating}, library book = {library_book}, format = {format_book}",
                  f"purchased = {purchased}")
            return 0
        except IndexError:
            print("You did not pass the correct # of arguments. Please use command --help")

    elif sys.argv[1] == "new":
        try:
            title = sys.argv[2]
            date_added = convert_date(sys.argv[3])

            print(f"adding to want to read: title = {title}, date added to TBR = {date_added}")
        except IndexError:
            print("You did not pass the correct # of arguments. Please use command --help")

    else:
        raise Exception("UNKNOWN COMMAND")
        #return 1 ?


rc = main()
sys.exit(rc)


#edit --> updating already placed records
#check --> see what data is missing
