from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

news_urls = {
    "English": "https://example.com/english_news",
    "Hindi": "https://example.com/hindi_news",
    "Mandarin": "https://example.com/mandarin_news",
}

def scrape_news(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('article')
        news_data = []
        for article in articles:
            headline = article.find('h2').text
            content = article.find('p').text
            news_data.append({"headline": headline, "content": content})
        return news_data
    except Exception as e:
        print("Error scraping news:", str(e))
        return []

@app.route('/')
def index():
    return render_template('base.html', languages=news_urls.keys())

@app.route('/get_news/<language>', methods=['POST'])
def get_news(language):
    if language in news_urls:
        news_data = scrape_news(news_urls[language])
    else:
        news_data = []
    return jsonify(news=news_data, language=language)

@app.route('/get_news/<language>',methods=['POST'])
def international(language):
    news_data = []
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
            news_data.append({"headline": headline})
    else:
        print('Failed to retrieve the webpage. Status code:', response.status_code)
    return news_data

if __name__ == '__main__':
    app.run(debug=True)
