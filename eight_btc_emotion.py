# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 16:11:50 2018

@author: v-beshi
"""
import get_all_links
import requests
from snownlp import SnowNLP
from bs4 import BeautifulSoup as bs
def get_8btc_emotion(pages):
    sen=[]
    user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers={'User-Agent':user_agent}
    links=get_all_links.get_all_links(pages)
    for link in links:
        page=requests.get(link,headers=headers)
        opt_page=bs(page.text)
        posts=opt_page.find_all('div',class_='t_fsz')
        for i in posts:
            s=SnowNLP(i.get_text())
            sentiment=s.sentiments
            sen.append(sentiment)
    total_sen=0
    count=0
    for i in sen:
        total_sen=total_sen+i
        count=count+1
    avg_sen=total_sen/count
    return(float(avg_sen))
        
            
