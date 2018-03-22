# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 15:06:58 2018

@author: v-beshi
"""
from sklearn.decomposition import IncrementalPCA
from sklearn.neural_network import MLPClassifier
import pandas as pd
from sklearn.externals import joblib
import time
import pandas as pd
import bfx
import huobi_USDT
import wallstreet_news
from okex2 import OKCoinFuture as ok
from preprocessing import d_pro

mykey=ok('www.okex.com','Public-Key','Private-Key')

def test_data(tt):
    pca=joblib.load('pca.m')
    next5=joblib.load('next5.m')
    next10=joblib.load('next10.m')
    next15=joblib.load('next15.m')
    i=0
    while i<=tt:
        try:
            DateTime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            ok0330=float(mykey.future_ticker('btc_usd','quarter')['ticker']['last'])
            ok_thisweek=float(mykey.future_ticker('btc_usd','this_week')['ticker']['last'])
            bfx_bids_wall=float(bfx.bfx_books()['bids_wall'])
            bfx_asks_wall=float(bfx.bfx_books()['asks_wall'])
            bfx_total_bids=float(bfx.bfx_books()['total_bids'])
            bfx_total_asks=float(bfx.bfx_books()['total_asks'])
            bfx_buy_volumn=float(bfx.bfx_volumn()[0])
            bfx_sell_volumn=float(bfx.bfx_volumn()[1])
            bfx_last_price=float(bfx.bfx_ticker())
            exchange_rate=float(mykey.exchange_rate()['rate'])
            huobiUSDT=float(huobi_USDT.get_usdt_price())
            #huobi USDT OTC price
            news_emotion=float(wallstreet_news.wallstr_news())
            #News emotion from wallstreet cn
            if i==0:
                raw=pd.DataFrame([[DateTime,ok0330,ok_thisweek,bfx_bids_wall,bfx_asks_wall,bfx_total_bids,bfx_total_asks,bfx_buy_volumn,bfx_sell_volumn,bfx_last_price,exchange_rate,huobiUSDT,news_emotion]],columns=['DateTime','ok0330','ok_thisweek','bfx_bids_wall','bfx_asks_wall','bfx_total_bids','bfx_total_asks','bfx_buy_volumn','bfx_sell_volumn','bfx_last_price','exchange_rate','huobi_USDT','news_emotion'])
            if (i>0)&(i<=15):
                raw2=pd.DataFrame([[DateTime,ok0330,ok_thisweek,bfx_bids_wall,bfx_asks_wall,bfx_total_bids,bfx_total_asks,bfx_buy_volumn,bfx_sell_volumn,bfx_last_price,exchange_rate,huobiUSDT,news_emotion]],index=[i],columns=['DateTime','ok0330','ok_thisweek','bfx_bids_wall','bfx_asks_wall','bfx_total_bids','bfx_total_asks','bfx_buy_volumn','bfx_sell_volumn','bfx_last_price','exchange_rate','huobi_USDT','news_emotion'])
                raw=raw.append(raw2)
            if i>15:
                raw3=pd.DataFrame([[DateTime,ok0330,ok_thisweek,bfx_bids_wall,bfx_asks_wall,bfx_total_bids,bfx_total_asks,bfx_buy_volumn,bfx_sell_volumn,bfx_last_price,exchange_rate,huobiUSDT,news_emotion]],index=[i],columns=['DateTime','ok0330','ok_thisweek','bfx_bids_wall','bfx_asks_wall','bfx_total_bids','bfx_total_asks','bfx_buy_volumn','bfx_sell_volumn','bfx_last_price','exchange_rate','huobi_USDT','news_emotion'])
                raw=raw.append(raw3)
                raw=raw.drop([i-16])
                feature=d_pro(raw) 
				#Data Preprocessing
                PCA_ed_feature=pca.transform(feature)
				#PCA Features
                next_5=next5.predict(PCA_ed_feature)[15]
                next_10=next10.predict(PCA_ed_feature)[15]
                next_15=next15.predict(PCA_ed_feature)[15]
				if next_5+next_10+next_15>2:
				#input auto-trading code to long
				if next_5+next_10+next_15=0:
				#input auto-trading code to short
				#predict the future bitcoin price(5min/10min/15min)
                print([next_5,next_10,next_15])
            i=i+1
            print(raw)
			time.sleep(60)
        except:
            print('connect error')          
    return raw