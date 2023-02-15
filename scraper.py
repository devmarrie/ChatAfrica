# import library
from bs4 import BeautifulSoup
import requests

# Request to website and download HTML contents
url='http://exploringafrica.matrix.msu.edu/activity-one-page-2-how-do-we-know-africa-has-a-history-engage/'
req=requests.get(url)
content=req.text

soup = BeautifulSoup(content)

html_code = soup.prettify()
    
with open('content/content-2.txt', 'w') as f:
    f.write(html_code)