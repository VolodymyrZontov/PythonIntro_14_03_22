import os


def create_folder_describe(folder: str) -> dict:
    folder_objects = os.listdir(folder)
    filenames = []
    subfolders = []
    for obj in folder_objects:
        obj_path = os.path.join(folder, obj)
        if os.path.isdir(obj_path):
            subfolders.append(obj)
        elif os.path.isfile(obj_path):
            filenames.append(obj)
    return {'filenames': filenames, 'dirnames': subfolders}


def sort_folder_objects(folder_objects: dict, without_reverse=True):
    for key in folder_objects:
        folder_objects[key].sort(reverse=not without_reverse)
    return folder_objects


def update_folder_objects(folder_objects: dict, obj_name: str):
    key = "filenames" if "." in obj_name else "dirnames"
    folder_objects[key].append(obj_name)
    return folder_objects


def compare_and_create_objects(folder_objects: dict, dirname: str):
    folder_objects_real = create_folder_describe(dirname)
    for filename in set(folder_objects["filenames"]).difference(set(folder_objects_real["filenames"])):
        with open(os.path.join(dirname, filename), 'w') as file:
            file.write('')
    for folder in set(folder_objects["dirnames"]).difference(set(folder_objects_real["dirnames"])):
        os.makedirs(os.path.join(dirname, folder))


fo = create_folder_describe("alphabet")
print(fo)

sort_fo = sort_folder_objects(fo, False)
print(sort_fo)

new_fo = update_folder_objects(fo, "qwe.txt")
new_fo = update_folder_objects(new_fo, "AAA")

compare_and_create_objects(fo, 'alphabet_2')


