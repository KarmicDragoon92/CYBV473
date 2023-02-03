'''
Week Two Assignment 4 - File Processing Object
Sundstrom Kaleb, 02/03/2023
'''


import os
from binascii import hexlify
from time import ctime

from hashing import HashFile          

from prettytable import PrettyTable
tbl = PrettyTable(['Path', 'FileSize', 'Hash', 'LastModified', 'FileHeader', 'Status', 'Error'])

class FileProcessor:
    

    def __init__(self, fileName):

        try:
            with open(fileName, 'rb') as binFile:
                header  = binFile.read(20)
                status = 'OK'
        except:
            status = 'Error'

        current_dir = os.getcwd()
        
        self.filePath         = current_dir + fileName
        self.lastModifiedTime = ctime(os.stat(fileName).st_mtime)
        self.fileSize         = os.stat(fileName).st_size
        self.md5Hash          = HashFile(fileName)
        self.fileHeader       = hexlify(header)
        self.status           = status
        self.errorInfo        = ''
        
    def GetFileMetaData(self):
        return self.filePath, self.fileSize, self.md5Hash, self.lastModifiedTime, self.fileHeader, self.status, self.errorInfo

def main():
        print("\nAssignment-4 Sundstrom\n")
        dirPath = input("Enter a valid directory path: ")
        for roots, dirs, files in os.walk(dirPath):
            for file in files:
                if os.path.isfile(file):
                    processed_file = FileProcessor(file) 
                tbl.add_row(processed_file.GetFileMetaData())
        print(tbl)
        tbl_string = tbl.get_string()
        with open('./SundstromK_WK3_prettytable.csv', 'w') as f:
            f.write(tbl_string)

if __name__ == '__main__':
    main()
    


        
        
        





        
        
