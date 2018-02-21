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
import pymssql
from okex2 import OKCoinFuture as ok
mykey=ok('www.okex.com','Public Key','Private Key')


def input_data(tt):
    trade_data=pd.DataFrame(columns=['time','ok0330','ok_thisweek','bfx_bids_wall','bfx_asks_wall','bfx_total_bids','bfx_total_asks','bfx_buy_volumn','bfx_sell_volumn','bfx_last_price','exchange_rate','huobi_USDT']) 
    for i in range(0,tt):
        t=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
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
        trade_data.loc[i]=[t,ok0330,ok_thisweek,bfx_bids_wall,bfx_asks_wall,bfx_total_bids,bfx_total_asks,bfx_buy_volumn,bfx_sell_volumn,bfx_last_price,exchange_rate,huobiUSDT]
        print(trade_data)
        time.sleep(30)
    trade_data.to_csv('btc.csv')
        