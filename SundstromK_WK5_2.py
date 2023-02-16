import re 
import os
from prettytable import PrettyTable 

words = re.compile(b'[a-zA-Z]{5,15}') 		# RE for strings 5 - 15 characters long
wordDict = {}								# Joke about how a Dict is a word Dict

wordTable = PrettyTable()
wordTable.field_names = ['Word', 'Occurences']

targetFile = input('File to scan: ')

with open(targetFile, 'rb') as file:
	for line in file:
		wordsFound = words.findall(line)
		for word in wordsFound:
			if word not in wordDict.keys():
				wordDict[word] = 1
			elif word in wordDict.keys():
				wordDict[word] += 1

for keys, values in wordDict.items():
	wordTable.add_row([keys, values])

wordTable.sortby = 'Occurences'
wordTable.reversesort = True
	
tableString = wordTable.get_string()

with open('./words.txt', 'w') as file:
	file.write(tableString)