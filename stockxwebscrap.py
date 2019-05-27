# import libraries
import urllib2
import csv
from bs4 import BeautifulSoup
from datetime import datetime

# specify the url
quote_page = 'http://www.bloomberg.com/quote/SPX:IND'

# query the website and return the html to the variable 'page'
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
name_box = soup.find('h1', attrs={'class': 'name'})

name = name_box.strip()
# strip() is used to remove starting and trailing

print name

# Take out the <div> of name and get its value
price_box = soup.find('div', attrs={'class': 'price'})

price = price_box.strip()
# strip() is used to remove starting and trailing

print price

# open a csv file with append, so old data will not be erased
with open('index.csv', 'a') as csv_file:
	writer = csv.writer(csv_file)
	writer.writerow([name, price, datetime.now()])