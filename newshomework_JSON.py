# -*- coding: utf-8 -*-
from collections import Counter
import json
from pprint import pprint

def most_common(lst):
    с = Counter(lst).most_common(10)
    return (с)

def writeshort(txt):
    wordlist = []
    for item in txt:
        if len(item) < 6:
            continue
        wordlist.append(item)
    return wordlist

with open ('newsafr.json', 'r', encoding = "utf-8") as f:
    x = json.load(f)
    pprint(x)



