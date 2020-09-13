import requests
from bs4 import BeautifulSoup
url='https://google.com'
response=requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')
rr=soup.findAll('a')
for t in rr:
    print(t['href'])
