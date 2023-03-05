from bs4 import BeautifulSoup
import requests
import os 

targetURL = 'https://casl.website/'

r = requests.get(targetURL)

soup = BeautifulSoup(r.text, 'html.parser')

webTitle = soup.title.string
links = soup("a")		# The short hand verison of soup.findAll(), returns a list
images = soup("img")

with open('WebContent.txt', 'w') as outFile:
	outFile.write(webTitle +"\n")
	for link in links:
		outFile.write(str(link) +'\n')
	for image in images:
		outFile.write(str(image['src'] +'\n'))

