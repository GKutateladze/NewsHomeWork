# -*- coding: utf-8 -*-
import chardet
import json
from collections import Counter

# Функция считает 10 самых повторяющихся слов
def most_common(lst):
    с = Counter(lst).most_common(10)
    return (с)

def get_news(text):
    data = open(text, 'rb').read()
    result = chardet.detect(data)
    charenc = result['encoding']
    news_list = []
    json_list = []
    with open(text, "r", encoding=charenc) as json_data:
        d = json.load(json_data)
        description = d['rss']['channel']['items']
        for value in description:
            json_list.append(value['description'])
    for item in json_list:
        x = item.split(" ")
        news_list += x

    wordlist = []
    for item in news_list:
        if len(item) < 6:
            continue
        wordlist.append(item)
    return wordlist

top_news = most_common(get_news("newsit.json"))
print(top_news)
top_news = most_common(get_news("newsafr.json"))
print(top_news)
top_news = most_common(get_news("newsfr.json"))
print(top_news)
top_news = most_common(get_news("newscy.json"))
print(top_news)

# Определено с помощью chardet
#newsafr.txt = utf-8
#newscy.txt = KOI8-R
#newsfr.txt = ISO-8859-5
#newsit.txt = cp1251