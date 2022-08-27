from datetime import date
import os
from PyPDF2 import PdfMerger
import pdfplumber
import os


files = os.listdir()
files.remove('export_data.py')
files.sort()



for file in files:
    # Get person name 
    # print(file)

    # Get person date of birth 
    # print(file)
  

    ######## Extract first name and last name ######## 
    try:
        with pdfplumber.open(r'/Users/ciprianpirvu/Downloads/Persons/102/' + file + "/" + file + ".pdf") as pdf:
            first_page = pdf.pages[0]
            text = first_page.extract_text()
            first_start_index = text.find("Date of Birth") + 16
            first_end_index = text.find("Data") - 1
            
            date_of_birth = text[first_start_index:first_end_index]

            print(date_of_birth)
            

    except:
        print("Something went wrong :( (1)")