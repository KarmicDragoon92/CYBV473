from PIL import Image
from prettytable import PrettyTable
import os

TARGET = input('Directory to process: ')

imtable = PrettyTable()
imtable.field_names = ["Image?", "File:", "File Size", "Ext", "Format", "Width", "Height", "Type"]

if os.path.isdir:
	for ROOT, DIR, FILE in os.walk(TARGET):
		for file in FILE:
			absPath = os.path.abspath(file)
			try:
				with Image.open(absPath) as im:
					file_ext = os.path.splitext(file)
					imtable.add_row(['YES', absPath, os.path.getsize(file), file_ext[1], im.format, im.width, im.height, im.mode ])

			except OSError:
				imtable.add_row(['NO', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA'])

else:
	print('That is not a valid directory.')

print(imtable)
