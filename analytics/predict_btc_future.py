# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 17:06:09 2018

@author: v-beshi
"""

import pyodbc
import pandas as pd
con=pyodbc.connect('DRIVER={SQL Server};SERVER=ServerName;DATABASE=DB;UID=ID;PWD=Password')
raw_data=pd.read_sql('select * from dbo.BitcoinTradeHistory',con)
raw_data=raw_data.drop(['DateTime','ok_thisweek'],axis=1)
qpre30=[]
for i in range(0,30):
    qpre30.append(0)
for i in range(30,len(raw_data)):
    qpre30.append((raw_data['ok0330'][i]-raw_data['ok0330'][i-30])/(raw_data['ok0330'][i-30]))
qpre30=pd.Series(qpre30,name='qpre30')

qpre20=[]
for i in range(0,20):
    qpre20.append(0)
for i in range(20,len(raw_data)):
    qpre20.append((raw_data['ok0330'][i]-raw_data['ok0330'][i-20])/(raw_data['ok0330'][i-20]))
qpre20=pd.Series(qpre20,name='qpre20')

qpre10=[]
for i in range(0,10):
    qpre10.append(0)
for i in range(10,len(raw_data)):
    qpre10.append((raw_data['ok0330'][i]-raw_data['ok0330'][i-10])/(raw_data['ok0330'][i-10]))
qpre10=pd.Series(qpre10,name='qpre10')

raw_data=pd.concat([raw_data,qpre30,qpre20,qpre10],axis=1)