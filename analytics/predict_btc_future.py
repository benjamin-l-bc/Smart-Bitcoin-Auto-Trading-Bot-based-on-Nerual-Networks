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
raw_data['0330pre-20']=0
for i in range(0,len(raw_data)):
    raw_data['0330pre-20'][20+i]=(raw_data['ok0330'][20+i]-raw_data['ok0330'][0+i])/raw_data['ok0330'][0+i]