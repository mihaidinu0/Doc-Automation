import os
import shutil

files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.pdf')]

path = "/Users/ciprianpirvu/Downloads/Persons/102/"
for file in files:

    src_path = path + file
    file_name = file.split(".")[0]
    file_name = file_name.split("-")[0] + ".pdf"
    print(file_name)
    # new_src_path = path + file
    os.rename(file, file_name)
    dest_path = path + file_name[:-4]
    try:
        if os.path.exists(dest_path):
            shutil.move(path + file_name, dest_path)
    except:
        print("There is no folder with that name: {}".format(file_name))




# print(files)