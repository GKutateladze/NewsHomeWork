# -*- coding: utf-8 -*-
from collections import Counter
# Функция считает 10 самых повторяющихся слов
def most_common(lst):
    с = Counter(lst).most_common(10)
    return (с)
# Функция добавляет в список все слова длиной более 6 символов
def writeshort(txt):
    wordlist = []
    for item in txt:
        if len(item) < 6:
            continue
        wordlist.append(item)
    return wordlist

newsafr_list = []
with open("newsafr.txt", "r", encoding = "utf-8") as f:
    afr = f.readlines()
    for item in afr:
        x = item.split(" ")
        newsafr_list += x

newscy_list = []
with open("newscy.txt", "r", encoding = "KOI8-R") as f:
    cy = f.readlines()
    for item in cy:
        x = item.split(" ")
        newscy_list += x

newsfr_list = []
with open("newsfr.txt", "r", encoding = "ISO-8859-5") as f:
    fr = f.readlines()
    for item in fr:
        x = item.split(" ")
        newsfr_list += x

newsit_list = []
with open("newsit.txt", "r", encoding = "cp1251") as f:
    it = f.readlines()
    for item in it:
        x = item.split(" ")
        newsit_list += x

newsafr = most_common(writeshort(newsafr_list))
newscy = most_common(writeshort(newscy_list))
newsfr = most_common(writeshort(newsfr_list))
newsit = most_common(writeshort(newsit_list))

print("NewsAFR:", newsafr)
print("NewsCY: ", newscy)
print("NewsFR: ", newsfr)
print("NewsIT: ", newsit)

# Определено с помощью chardet
#newsafr.txt = utf-8
#newscy.txt = KOI8-R
#newsfr.txt = ISO-8859-5
#newsit.txt = cp1251

# Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для каждого файла.
# Не забываем про декомпозицию и организацию кода в функции. В решении домашнего задания вам могут помочь: split(), sort() или sorted().

