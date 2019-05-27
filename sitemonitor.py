# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time

# Import smtplib (to allow us to email)
import smtplib

while True:
    # set the url as VentureBeat,
    url = "http://yeezysupply.com"
    # set the headers like we are a browser,
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # download the homepage
    response = requests.get(url, headers=headers)
    # parse the downloaded homepage and grab all text, then,
    soup = BeautifulSoup(response.text, "lxml")
    
    # if the number of times the word "Google" occurs on the page is less than 1,
    if str(soup).find("glow") >= 10:
        # wait 60 seconds,
        time.sleep(5)
        # continue with the script,
        print('Does this work')
        continue
        
    # but if the word "Google" occurs any other number of times,
    else:
        # create an email message with just a subject line,
        msg = 'Subject: This is Tre\'s script talking, CHECK GOOGLE!'
        # set the 'from' address,
        fromaddr = 'tre1234@mailinator.com'
        # set the 'to' addresses,
        toaddrs  = ['tre1234@mailinator.com']

        # Print the email's contents
        print('From: ' + fromaddr)
        print('To: ' + str(toaddrs))
        print('Message: ' + msg)
        
        break