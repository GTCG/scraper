from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import string
import urllib


urllist=[]
url1="http://www.bisy.be/"

fname = "test2.txt"
fh = open(fname)
for line in fh:
	line = line.rstrip()
	if line.startswith(" <tr class="):
		words= line.split()
		url2 = words[6]
		url3 = url1 + url2[1:48]
		urllist.append(url3)

        
for link in urllist:
	document = urllib.request.urlopen(link)
	html = document.read()
	soup = BeautifulSoup(html,"html.parser")
	elements = soup.find_all("p")
	elements2 = soup.find_all("p")
	for tag2 in elements2:
		try:
			if "color:#000000; font-size: 16pt; font-family: Arial;text-align:left;align:left" in tag2["style"]:
				details2 = tag2.text
				print(details2)
				f= open("adressen.txt","a")
				f.write(details2)
				f.close
				
		except:
			pass
	for tag in elements:
		try:
			if "9pt" in tag["style"]:
				details = tag.text
				print(details)
				f= open("adressen.txt","a")
				f.write(details)
				f.close
		except:
			pass
