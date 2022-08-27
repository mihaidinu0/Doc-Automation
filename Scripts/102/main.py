import pdfplumber
import os
import shutil


files = os.listdir()

# Iterate over all the files in directory
for file in files:

    try:
    ######## Extract first name and last name ######## 
        with pdfplumber.open(r'/Users/ciprianpirvu/Downloads/Persons/Last/' + file) as pdf:
            first_page = pdf.pages[0]
            text = first_page.extract_text()
            first_start_index = text.find("First Name: ") + 13
            first_end_index = text.find("Prenumele") - 1
            first_name = text[first_start_index:first_end_index].strip()
            
            last_start_index = text.find("Last Name: ") + 12
            last_end_index = text.find("Numele: ") - 1
            last_name = text[last_start_index:last_end_index].strip()
            
            file_name = first_name + " " + last_name + ".pdf"
            print(file_name)
    except:
        print("Something went wrong :(")

    # Renaming the file
    os.rename(file, file_name)







# ######## Create directories with CV name ########
# # Parent Directory path
path = "/Users/ciprianpirvu/Downloads/Persons/Last"
dir_list = os.listdir(path)
 

for directory in dir_list:
    # Path
    path = "/Users/ciprianpirvu/Downloads/Persons/Last/" + directory.split('.')[0]
    # Create the directory
    try:
        os.mkdir(path)
        src_path = "/Users/ciprianpirvu/Downloads/Persons/Last/" + directory
        dst_path = "/Users/ciprianpirvu/Downloads/Persons/Last/" + directory.split('.')[0]
        shutil.move(src_path, dst_path)
    except:
        print("Something went wrong :(") 
        
    print("Directory '%s' created" % path)





