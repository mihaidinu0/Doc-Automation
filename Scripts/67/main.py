# Python program to explain os.mkdir() method
	
# importing os module
import os
import shutil

# # Directory
# 
# # Parent Directory path
path = "/Users/ciprianpirvu/Downloads/Persons/First"
dir_list = os.listdir(path)
 

for directory in dir_list:
    # Path
    # path = os.path.join(path, (directory.split('.')[0]))
    path = "/Users/ciprianpirvu/Downloads/Persons/First/" + directory.split('.')[0]
    # Create the directory
    try:
        os.mkdir(path)
        src_path = "/Users/ciprianpirvu/Downloads/Persons/First/" + directory
        dst_path = "/Users/ciprianpirvu/Downloads/Persons/First/" + directory.split('.')[0]
        shutil.move(src_path, dst_path)


    except OSError as error:
        print(error) 
        
    print("Directory '%s' created" % path)


# absolute path



