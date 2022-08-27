from PyPDF2 import PdfMerger
import pdfplumber
import os
import shutil
from natsort import natsorted

files = natsorted(os.listdir())[1:]
files.remove('main.py')
# Create and instance of PdfFileMerger() class


merger = PdfMerger()
counter = 0
index = 0
for pdf in files:
    merger.append(pdf)
    os.system(f"rm -rf " + str(pdf))
    counter += 1    
    if counter == 2:
        pdf_name = "result" + str(index) + ".pdf"
        merger.write(pdf_name)
        index += 1
        counter = 0
        merger.close()

        merger = PdfMerger()

        ######## Extract first name and last name ######## 
        try:
            with pdfplumber.open(r'/Users/ciprianpirvu/Downloads/New/Persons/' + pdf_name) as pdf:
                first_page = pdf.pages[0]
                text = first_page.extract_text()
                first_start_index = text.find("First Name: ") + 13
                first_end_index = text.find("Prenumele") - 1
                first_name = text[first_start_index:first_end_index].strip()
                # print(first_name)
                
                last_start_index = text.find("Last Name: ") + 12
                last_end_index = text.find("Numele: ") - 1
                last_name = text[last_start_index:last_end_index].strip()
                # print(last_name)
                
                file_name = first_name + " " + last_name + ".pdf"
        except:
            print("Something went wrong :( (1)")

        # Renaming the file
        os.rename(pdf_name, file_name)

        path = "/Users/ciprianpirvu/Downloads/New/Persons/" + file_name.split('.')[0]
        # Create the directory
        try:
            os.mkdir(path)
            src_path = "/Users/ciprianpirvu/Downloads/New/Persons/" + file_name
            dst_path = "/Users/ciprianpirvu/Downloads/New/Persons/" + file_name.split('.')[0]
            shutil.move(src_path, dst_path)
            
        except:
            print("Something went wrong :( (2)") 
            



    












