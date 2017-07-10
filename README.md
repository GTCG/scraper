# scraper
Data scraper to scrape data from Belgian companies.

I needed specific data from certain companies in Belgium. Therefore I used the website www.bisy.be and checked the page sources to find the URL's of the companies I was looking for.

I copied and pasted the revelant parts in the pagesources.txt file. You need this file if you want to run this program yourself (not to forget beautifulsoup and other modules.) 
The links leading to the companies are being stored in a list. After that, the relevant data for each company is being pulled in, and parsed in another txt file, being called "addressen.txt".

After that you can easily export everything to a Word or excel file if you like. Due to lack of time, I was unable to implement this in the program, but that is something I will do in the near future.

This program is written in Python 3.5. Use PIP if you need to install additional modules.
T.
