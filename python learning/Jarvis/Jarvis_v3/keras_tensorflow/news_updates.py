import json,requests
from speak import *


def news():
    url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey='+NEWS_API_KEY)
    response = requests.get(url).json()['articles']
    news_article = []
    for i in response:
        news_article.append(i['title'])
    for j in range(5):
        print(j+1,news_article[j])
        speak(news_article[j])
 