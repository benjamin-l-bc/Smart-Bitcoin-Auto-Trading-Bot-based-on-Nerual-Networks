# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 17:20:58 2018

@author: v-beshi
"""

import requests
import json
import time
import pandas as pd
from matplotlib import pyplot as plt
def get_usdt_price():
    user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers={'User-Agent':user_agent}
    page=requests.get("https://api-otc.huobi.pro/v1/otc/trade/list/public?coinId=2&tradeType=1&currentPage=1&payWay=&country=&merchant=0&online=1&range=0",headers=headers)
    otc=json.loads(str(page.text))
    ttp=0
    tta=0
    for i in range(0,10):
        USDT_price=otc['data'][i]['price']*otc['data'][i]['tradeCount']
        amount=otc['data'][i]['tradeCount']
        ttp=ttp+USDT_price
        tta=tta+amount
    usdt=ttp/tta
    return(usdt)
