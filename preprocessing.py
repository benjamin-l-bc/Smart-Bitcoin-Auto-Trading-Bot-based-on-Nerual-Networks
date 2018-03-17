# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 20:55:57 2018

@author: v-beshi
"""
import pandas as pd

def d_pro(raw_data):
    #input the data resource

    raw_data['USDT_exceed']=raw_data['huobi_USDT']-raw_data['exchange_rate']
    
    lastloc=raw_data.index.get_values()[len(raw_data.index.get_values())-1]
    firstloc=raw_data.index.get_values()[0]
    
    pre_price15=[]
    for i in range(0,14):
        pre_price15.append(0)
    pre_price15.append((raw_data['ok0330'][lastloc]-raw_data['ok0330'][firstloc])/(raw_data['ok0330'][firstloc]))
    pre_price15=pd.Series(pre_price15,name='pre_price15')

    pre_price10=[]
    for i in range(0,14):
        pre_price10.append(0)
    pre_price10.append((raw_data['ok0330'][lastloc]-raw_data['ok0330'][lastloc-10])/(raw_data['ok0330'][lastloc-10]))
    pre_price10=pd.Series(pre_price10,name='pre_price10')

    pre_price5=[]
    for i in range(0,14):
        pre_price5.append(0)
    pre_price5.append((raw_data['ok0330'][lastloc]-raw_data['ok0330'][lastloc-5])/(raw_data['ok0330'][lastloc-5]))
    pre_price5=pd.Series(pre_price5,name='pre_price5')

    pre_bfx=[0]
    for i in range(0,14):
        pre_bfx.append(0)
    pre_bfx.append((raw_data['bfx_last_price'][lastloc]-raw_data['bfx_last_price'][lastloc-1])/(raw_data['bfx_last_price'][lastloc-1]))
    pre_bfx=pd.Series(pre_bfx,name='pre_bfx')

    pre_news10=[]
    for i in range(0,14):
        pre_bfx.append(0)
    pre_news10.append((raw_data['news_emotion'][lastloc]-raw_data['news_emotion'][lastloc-10])/(raw_data['news_emotion'][lastloc-10]))
    pre_news10=pd.Series(pre_news10,name='pre_news10')
    
    raw_data['bids_wall']=raw_data['bfx_bids_wall']/100
    raw_data['asks_wall']=raw_data['bfx_asks_wall']/100
    raw_data['total_bids']=raw_data['bfx_total_bids']/100
    raw_data['total_asks']=raw_data['bfx_total_asks']/100
    raw_data['buy_volumn']=raw_data['bfx_buy_volumn']/50
    raw_data['sell_volumn']=raw_data['bfx_sell_volumn']/50

    raw_data=raw_data.drop(['ok0330','DateTime','ok_thisweek','huobi_USDT','exchange_rate','bfx_last_price','news_emotion','bfx_bids_wall','bfx_asks_wall','bfx_total_bids','bfx_total_asks','bfx_buy_volumn','bfx_sell_volumn'],axis=1)
    agg_data=pd.concat([raw_data,pre_price15,pre_price10,pre_price5,pre_bfx,pre_news10],axis=1)
    return(agg_data)