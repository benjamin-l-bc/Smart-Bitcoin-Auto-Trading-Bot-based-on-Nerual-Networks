# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 22:29:34 2018

@author: v-beshi
"""

import requests
from bs4 import BeautifulSoup as bs
import re
from snownlp import SnowNLP
def wallstr_news():
    user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers={'User-Agent':user_agent}
    url='https://wallstreetcn.com/live/blockchain'
    raw_page=requests.get(url,headers=headers)
    page=bs(raw_page.text)
    blockchain_news=page.find_all('div',class_="wscn-tab-pane")[1]
    big_news=blockchain_news.find_all('div',class_='live-item score-2')
    normal_news=blockchain_news.find_all('div',class_='live-item score-1')
    s=0
    count=0
    for i in big_news:
        text=i.find('div',class_='content-html').get_text()
        sen=SnowNLP(text)
        sentiment=sen.sentiments
        s=s+2*sentiment
        count=count+2
    for i in normal_news:
        text=i.find('div',class_='content-html').get_text()
        sen=SnowNLP(text)
        sentiment=sen.sentiments
        s=s+sentiment
        count=count+1
    total_sentiment=s/count
    return(total_sentiment)
