from datetime import datetime

def read_txt_file(filename: str) -> list:
    with open(filename, 'r') as txt_file:
        data = txt_file.read().splitlines()
    return data


def get_domains(filename: str):
    data = read_txt_file(filename)
    domains = [line.replace(".", "") for line in data]
    return domains


def get_names(filename: str):
    data = read_txt_file(filename)
    names = [line.split("\t")[1] for line in data]
    return names


def get_authors_dates(filename: str):
    data = read_txt_file(filename)
    dates = []
    for line in data:
        if " - " in line and line[:1].isdigit():
            dates.append({"date": line.split(" - ")[0]})
    return dates


def transform_date(author_date: str):
    # months_dict = {"January": "01",
    #                "February": "02",
    #                "March": "03",
    #                "April": "04",
    #                "May": "05",
    #                "June": "06",
    #                "July": "07",
    #                "August": "08",
    #                "September": "09",
    #                "October": "10",
    #                "November": "11",
    #                "December": "12"}
    # day, month, year = author_date.split()
    # day = day[:-2].zfill(2)
    # month = months_dict[month]
    # return f"{day}/{month}/{year}"
    day, month, year = author_date.split()
    day = day[:-2].zfill(2)
    date = f"{day} {month} {year}"
    new_date = datetime.strptime(date, "%d %B %Y").strftime("%d/%m/%Y")
    return new_date




def get_modified_dates(filename: str):
    dates = get_authors_dates(filename)
    new_dates = []
    for author_date in dates:
        date = author_date["date"]
        new_dates.append({"date_original": date, "date_modified": transform_date(date)})
    return new_dates


domains = get_domains("Homeworks/domains.txt")
names = get_names("Homeworks/names.txt")
dates = get_authors_dates("Homeworks/authors.txt")
modified_dates = get_modified_dates("Homeworks/authors.txt")

print(domains)
print(names)
print(dates)
print(modified_dates)
