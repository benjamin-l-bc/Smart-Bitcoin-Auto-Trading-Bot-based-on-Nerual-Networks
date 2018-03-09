# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 13:27:04 2018

@author: v-beshi
"""

import requests
import json
import time
import pandas as pd
import bfx
import huobi_USDT
import wallstreet_news
from okex2 import OKCoinFuture as ok
import eight_btc_emotion
import pyodbc
mykey=ok('www.okex.com','Public-Key','Private-Key')
#replace the Public-Key and Private-Key with your OKex API access
con=pyodbc.connect('DRIVER={SQL Server};SERVER=server;DATABASE=db;UID=id;PWD=password')
#connect to SQL Server Database
def input_data(tt):
    #input the number of rows you want to input
	j=0
    for i in range(0,tt):
        #count number of rows
        try:
            ok0330=float(mykey.future_ticker('btc_usd','quarter')['ticker']['last'])
            ok_thisweek=float(mykey.future_ticker('btc_usd','this_week')['ticker']['last'])
            bfx_bids_wall=bfx.bfx_books()['bids_wall']
            bfx_asks_wall=bfx.bfx_books()['asks_wall']
            bfx_total_bids=bfx.bfx_books()['total_bids']
            bfx_total_asks=bfx.bfx_books()['total_asks']
            bfx_buy_volumn=bfx.bfx_volumn()[0]
            bfx_sell_volumn=bfx.bfx_volumn()[1]
            bfx_last_price=bfx.bfx_ticker()
            exchange_rate=float(mykey.exchange_rate()['rate'])
            huobiUSDT=float(huobi_USDT.get_usdt_price())
            #get USDT price from huobi.pro
            news_emotion=float(wallstreet_news.wallstr_news())
            #get news emotion from wallstreet news blockchain channel
            e_btc_emotion=float(eight_btc_emotion.get_8btc_emotion(1))
            #get emotion from 8btc
            cursor=con.cursor()
            cursor.execute("insert into dbo.BitcoinTradeHistory values(getdate(),{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12})".format(ok0330,ok_thisweek,bfx_bids_wall,bfx_asks_wall,bfx_total_bids,bfx_total_asks,bfx_buy_volumn,bfx_sell_volumn,bfx_last_price,exchange_rate,huobiUSDT,news_emotion,e_btc_emotion))
            #insert into SQL Server Database
            con.commit()
            j=j+1
            print('collected {0} rows'.format(j))
            time.sleep(120) 
        except:
            print('connect error')             
    print('done')