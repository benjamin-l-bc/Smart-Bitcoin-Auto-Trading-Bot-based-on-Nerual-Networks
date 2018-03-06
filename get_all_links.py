# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 14:59:54 2018

@author: v-beshi
"""
import requests
from bs4 import BeautifulSoup as bs

import time
import re

def get_all_links(pages):
    links=[]
    user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers={'User-Agent':user_agent}
    for i in range(1,pages+1):
        url='http://8btc.com/forum-61-{pages}.html'.format(pages=i)
        page=requests.get(url,headers=headers)
        opt_page=bs(page.text)
        dis=opt_page.find_all(class_='discuz-list clearfix')
        for j in dis:
            title=j.find_all('a',class_='s xst')
            for k in title:
                if k.attrs['href'].startswith('http://8btc.com/thread'):
                    links.append(k.attrs['href'])
    return(links)
    


                    
                    
                    
                
            
        
        

    