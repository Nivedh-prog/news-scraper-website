import requests
from bs4 import BeautifulSoup
count = 0
url = 'https://zeenews.india.com/hindi'
response = requests.get(url)
print(response.status_code)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    headline_elements1 = soup.find_all('div',{'class':'news_description'})
    headline_elements2 = soup.find_all('div',{'class':'medium-thumb-list'})
    for headline in headline_elements1:
        headline_text = headline.get_text().strip()
        print(headline_text)
        count=count+1
    for headline in headline_elements2:
        headline_text = headline.get_text().strip()
        print(headline_text)
        count=count+1
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)
