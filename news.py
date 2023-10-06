import requests
from bs4 import BeautifulSoup
count = 0
def international():
    count = 0
    url = 'https://www.1stheadlines.com/index.htm'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    if response.status_code == 200:
        headline_elements = soup.find_all('a',class_='hed')
    while count<10:
        for headline in headline_elements:
            headline_text = headline.get_text().strip()
            print(headline_text)
            count=count+1
    else:
        print('Failed to retrieve the webpage. Status code:', response.status_code)


def national():
    url = 'https://www.indiatoday.in/india'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(response.status_code)

    if response.status_code == 200:
        headline_elements = soup.find_all('div',{'class':'B1S3_content__wrap__9mSB6'})
        for headline in headline_elements:
                headline_text = headline.get_text().strip()
                print(headline_text)
                count=count+1
    else:
        print('Failed to retrieve the webpage. Status code:', response.status_code)


def hindi():
    count = 0
    url = 'https://zeenews.india.com/hindi'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(response.status_code)

    if response.status_code == 200:
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

def malayalam():
    url = 'https://www.manoramaonline.com/news/latest-news.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    print(response.status_code)
    if response.status_code == 200:
        headline_elements = soup.find_all('div',{'class':'story-content-blk'})
        for headline in headline_elements:
                headline_text = headline.get_text().strip()
                print(headline_text)
                count=count+1
    else:
        print('Failed to retrieve the webpage. Status code:', response.status_code)
def assam():
    count = 0
    url = 'https://www.asomiyapratidin.in/'
    response = requests.get(url)
    print(response.status_code)
    soup = BeautifulSoup(response.text, 'html.parser')

    if response.status_code == 200:
        headline_elements = soup.find_all('div',{'class':'arrow-component arr--headline'})
        for headline in headline_elements:
                headline_text = headline.get_text().strip()
                print(headline_text)
                count=count+1
    else:
        print('Failed to retrieve the webpage. Status code:', response.status_code)
