import pdfplumber
import pandas as pd

#function to read the number of pages
def number_of_pages(filename):

        with pdfplumber.open(filename) as pdf:
        #with pdfplumber.open("harness/_n4wl99z.pdf") as pdf:       
                #data_table =  pdf.pages[2].extract_table()
                for tables in pdf.pages:
                        print('Pages in PDF files: ',tables)