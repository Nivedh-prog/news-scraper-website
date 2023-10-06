import requests
from bs4 import BeautifulSoup
count = 0
url = 'https://www.manoramaonline.com/news/latest-news.html'

response = requests.get(url)
print(response.status_code)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    headline_elements = soup.find_all('div',{'class':'story-content-blk'})
    for headline in headline_elements:
            headline_text = headline.get_text().strip()
            print(headline_text)
            count=count+1
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)
