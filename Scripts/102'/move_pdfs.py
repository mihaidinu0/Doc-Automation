import os
import shutil

files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.pdf')]

path = "/Users/ciprianpirvu/Downloads/Persons/102/"
for file in files:
    directory_name = file[:-4]
    file_name = file.split(".")[0] + "_offer.pdf"
    os.rename(file, file_name)
    dest_path = path + directory_name
    try:
        if os.path.exists(dest_path):
            shutil.move(path + file_name, dest_path)
    except:
        print("There is no folder with that name: {}".format(dest_path))




# print(files)