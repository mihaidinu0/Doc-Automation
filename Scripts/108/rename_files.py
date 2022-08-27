import os
import re


files = os.listdir()
files.remove('rename_files.py')
files.remove('main.py')

path = '/Users/ciprianpirvu/Downloads/Persons/102/'
regex_passport = re.compile('Passport*')
regex_photo = re.compile('Photo') # De verificat sa nu fie pdf...


for file in files:
    file_path = path + file
    if file != '.DS_Store':
        directory_files = os.listdir(file_path)
        for dir_file in directory_files:
            # if regex_passport.match(dir_file):
            #     src_path = path + file + "/" + dir_file
            #     dest_path = path + file + "/Passport.pdf"
            #     os.rename(src_path, dest_path)
            if regex_photo.match(dir_file):
                src_path = path + file + "/" + dir_file
                dest_path = path + file + "/Photo.pdf"
                os.rename(src_path, dest_path)
