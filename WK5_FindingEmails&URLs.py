'''
Sundstrom K, Week5, Finding emails and URLs
February 15, 2023
'''

import re 
import os
from prettytable import PrettyTable 

emailRE = re.compile(b'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}')  # Regular Expression for Emails
urlRE = re.compile(b'\w+:\/\/[\w@][\w.:@]+\/?[\w.\.?=%&=\-@$,]*')		  # Regular Expression for URL's

emailtbl = PrettyTable()
emailtbl.field_names = ['Email', 'Occurences']		# A pretty table for our emails

urltbl = PrettyTable()
urltbl.field_names = ['URL', 'Occurences']

emailDict = {}
urlDict = {}

targetBin = input('Please enter bin file to search: ')

with open(targetBin, 'rb') as file:
	for line in file:
		emails = emailRE.findall(line)
		urls = urlRE.findall(line)
		if emails:
			for email in emails:
				try:
					occurences = emailDict[email] 
					occurences += 1
					emailDict[email] = occurences
				except:
					occurences = 1
					emailDict[email] = occurences

			

		if urls:
			for url in urls:
				try:
					occurences = urlDict[url] 
					occurences += 1
					urlDict[url] = occurences
				except:
					occurences = 1
					urlDict[url] = occurences


for key, value in emailDict.items():
	emailtbl.add_row([key, value])		# Populate email pretty table


for key, value in urlDict.items():
	urltbl.add_row([key, value])		# Populate URL pretty table
			



print(emailtbl)
print(urltbl)
