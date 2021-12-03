# Rodrigo Alcover
# 7/11/2021
# CIS-216-12292 
# Python Programming


from collections import Counter
from typing import List

class CSVReport:
    
    def __init__(self):
        self.reading = 'read_csv'

    def read_csv(self):
        header = True  
        year_data = {}
        print("Year |  Min |  Max |  Avg") #header 
        print("==== | ==== | ==== | ====")
        with open('MIGRNDRA.csv', 'r') as my_file:# Open file for reading with open(path)
            for line in my_file.readlines():#search for lines 
                line = line.strip() #   
                if not line: 
                    continue
                if header:#search for header
                    header = False#ignore the header
                    continue
                values = line.split(',')#How to read the values separated by a coma
                month = int(values[0])#read and store values
                day = int(values[1])
                year = int(values[2])
                temp = float(values[3])
                if year not in year_data:#load year 
                    year_data[year] = []# add year to the collection
                year_data[year].append(temp) #append the dictionary    
      

                continue        
           
        for year, temps in year_data.items():#read year and temps
         
            average = sum (temps) / len(temps)#calculate average
            minimun = min (temps) #calulate minimun
            maximun = max (temps)#calculate max
        
                
            print("{} | {:=4} | {:>.1f} | {:>.1f}".format (year, minimun, maximun, average))#Print the results
#How to read the values
        
my_csv_instance = CSVReport()
my_csv_instance.read_csv()


    
    