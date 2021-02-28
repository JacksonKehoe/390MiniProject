import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen


#ticker

userticker = input('Enter any ticker: ')
ticker = 'aapl'
#url

urlStart = 'https://finviz.com/quote.ashx?t='
urlEnd = '&ty=c&ta=1&p=d'
URL = urlStart + userticker.lower()

#web request and info collection
headers = {'User-Agent': 'Mozilla/5.0'}
request = Request(URL, headers=headers) #note that urllib is needed to add a user header for user validation)
web = urlopen(request).read()
#storing the info in two formsnmb
html = soup(web, "html.parser")
xml = soup(web, "xml")

#reading values into a table
#print(xml)
tableStart = pd.read_html(str(html), attrs = {'class': 'snapshot-table2'})[0]
#tableStart.to_excel(r'C:\Testing\bitch.xlsx', index = False) #did testing with appl, use whichever path and file name you want, or comment this line out

print(tableStart)
