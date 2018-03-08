# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 22:14:26 2018

@author: v-beshi
"""

import requests
import json
def bfx_ticker():
    url1 = "https://api.bitfinex.com/v2/ticker/tBTCUSD"
    response_ticker = requests.request("GET", url1)
    split=response_ticker.text.split(',')
    last_price=split[6]
    return(last_price)
def bfx_volumn():
    url3 = "https://api.bitfinex.com/v1/trades/btcusd"
    response_trades = requests.request("GET", url3)
    volumn=json.loads(response_trades.text)
    buy_volumn=0
    sell_volumn=0
    for i in volumn:
        if i['type']=='buy':
            buy_volumn=buy_volumn+float(i['amount'])
        else:
            sell_volumn=sell_volumn+float(i['amount'])
    return(buy_volumn,sell_volumn)
def bfx_books():
    url2 = "https://api.bitfinex.com/v1/book/btcusd"
    response_book = requests.request("GET", url2)
    books=json.loads(response_book.text)
    bids_wall=0
    asks_wall=0
    total_bids=0
    total_asks=0
    bids=books['bids']
    asks=books['asks']
    for i in bids:
        if float(i['amount'])>bids_wall:
            bids_wall=float(i['amount'])
        total_bids=total_bids+float(i['amount'])
    for i in asks:
        if float(i['amount'])>asks_wall:
            asks_wall=float(i['amount'])
        total_asks=total_asks+float(i['amount'])
    books_result={}
    books_result['bids_wall']=bids_wall
    books_result['asks_wall']=asks_wall
    books_result['total_bids']=total_bids
    books_result['total_asks']=total_asks
    return(books_result)
    

