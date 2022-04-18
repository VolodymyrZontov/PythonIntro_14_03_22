persons = [{"name": "david", "age": 2},
           {"name": "david1234", "age": 5},
           {"name": "Johna", "age": 15},
           {"name": "alexander", "age": 2}]
max_age = persons[0]["age"]
max_len = len(persons[0]["name"])
max_age_names = []
max_len_names = []
for person in persons:
    if person["age"] < max_age:
        name_max_len = person["age"]
        max_age_names = [person["name"]]
    elif person["age"] == max_age:
        max_age_names.append(person["name"])
    if person["name"] > max_len:
        name_max_len = person["name"]
        max_len_names = [person["name"]]
    elif person["name"] == max_len:
        max_len_names.append(person["name"])


