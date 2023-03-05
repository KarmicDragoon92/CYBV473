
'''
Week Two Assignment - File Hashing
Kaleb Sundstrom, 2023-01-2023
'''


import os
import hashlib
from prettytable import PrettyTable

def hash_file(FILE):
    with open(FILE, 'rb') as FILE_Hash:
        fileContents = FILE_Hash.read()
        hashObj = hashlib.md5()
        hashObj.update(fileContents)
        hashed_file = hashObj.hexdigest()
        return hashed_file

hash_table = PrettyTable()
hash_table.field_names = ['Hash Value', 'File Path']      

DIR = input('Input file path for dir you would like to walk: ')

fileList   = []
fileHashes = {}

for root, dirs, files in os.walk(DIR):

    print(root)
    print(dirs)
    print(files)
    
    for fileName in files:
        path = os.path.join(root, fileName)
        fullPath = os.path.abspath(path)
        fileHash = hash_file(fullPath)
        fileHashes[fileHash] = fullPath

for keys, values in fileHashes.items():
    hash_table.add_row([keys, values])
      
print(hash_table)
        
        
