# -*- coding: utf-8 -*-
import chardet
from collections import Counter

# Функция считает 10 самых повторяющихся слов
def most_common(lst):
    с = Counter(lst).most_common(10)
    return (с)

def get_news(text):
    news_list = []
    data = open(text, 'rb').read()
    result = chardet.detect(data)
    charenc = result['encoding']
    with open(text, "r", encoding=charenc) as f:
        r = f.readlines()
        for item in r:
            x = item.split(" ")
            news_list += x

    wordlist = []
    for item in news_list:
        if len(item) < 6:
            continue
        wordlist.append(item)
    return wordlist

top_news = most_common(get_news("newsfr.txt"))
print(top_news)

# Определено с помощью chardet
#newsafr.txt = utf-8
#newscy.txt = KOI8-R
#newsfr.txt = ISO-8859-5
#newsit.txt = cp1251

# Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для каждого файла.
# Не забываем про декомпозицию и организацию кода в функции. В решении домашнего задания вам могут помочь: split(), sort() или sorted().

