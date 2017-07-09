import sqlite3 
import re
import urllib2
from urllib2 import Request, urlopen, URLError
from bs4 import BeautifulSoup
import requests
import string
import urllib

conn = sqlite3.connect('bedrijven.sqlite')
conn.text_factory = str
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS bedrijven")
cur.execute("CREATE TABLE bedrijven ( id integer primary key, Naam text, straat text, tel text, fax text, email text, web text)")
conn.commit()

urllist=[]
url1="http://www.bisy.be/"

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "test.txt"

fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    if line.startswith(" <tr class="):
        count = count + 1
        words= line.split()
        url2 = words[6]
        url3 = url1 + url2[1:48]
        urllist.append(url3)
        
for link in urllist:        
    lines = urllib.request.urlopen(url3)
    bedrijfdata = lines.read()
    lines.close()
    soup = BeautifulSoup(bedrijfdata,"html.parser")
    for link in soup.findall('a'):
        print link.get('href')
    
