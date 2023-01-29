
'''
Week Two Assignment - File Processing
Kaleb Sundstrom, 2023-01-25
'''

import os
from prettytable import PrettyTable

uniqueWorms = {}
uniqueWormsTable = PrettyTable()

uniqueWormsTable.field_names = ['Worms Name', 'Number of Occurences']

with open("redhat.txt", 'r') as logFile:
    for eachLine in logFile:
        eachLineLower = eachLine.lower()
        fieldList = eachLineLower.split()
        for eachField in fieldList:
            if 'worm' in eachField:
                if eachField not in uniqueWorms:
                    uniqueWorms[eachField] = 1
            if eachField in uniqueWorms:
                uniqueWorms[eachField] += 1

for k, v in uniqueWorms.items():
    uniqueWormsTable.add_row([k, v])

print(uniqueWormsTable)
                
                
            
            
    


        
        
