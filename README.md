# bitcoin autotrade - OKex
## 目标是用机器学习自动交易okex的bitcoin季度和周的期货合约进行套利。
## The goal for this programme is to autotrade the future in OKex thru machine learning result.
##### 1. 按照时间120秒间隔抓取OKEX，huobi_USDT,bfx上现货价格。
#####    get 1)the trade data from Okex,bfx. 2)USDT OTC price from Huobi.pro 3).Emotion from News and Forum
##### 2. 用sklearn进行机器学习找出最佳策略最大化收益。
#####    find the best trading strategy thru machine learning using sklearn to optimize profit.
##### 3. 用okex API进行自动交易。
#####    AutoTrade Okex Bitcoin future thru Okex API

## run input_data.py

需要提前安装
You need to install below packages before run input_data.py
<br>`pip install sklearn` -- For machine learning purpose
<br>`pip install requests` -- Access to webpage
<br>`pip install BeautifulSoup` -- Formalize webpage
<br>`pip install snownlp` -- Analyze emotion of sentenses in Chinese
<br>`pip install pyodbc` -- connect to SQL Server DB

代码尚未完成并会不断进行完善~ Will update the code from time to time.

###### Updates 3/6/2018 
<br> 1.从华尔街见闻的区块链频道抓取新闻，使用SnowNLP分析新闻的情绪，news_emotion作为最后分析的feature
<br> get the news from wallstreet cn(https://wallstreetcn.com/) blockchain channel. Analyze the emotion thru SnowNLP. Input as a feature.
<br> 2.从8btc论坛抓取新闻，使用SnowNLP分析论坛帖子和回帖的情绪，8btc_emotion作为最后分析的feature
<br> get the posts from Chinese biggest BTC forum--8btc cn(https://8btc.com/) blockchain channel. Analyze the emotion thru SnowNLP. Input as a feature.
(Will Update and input the emotion from Reddit in the future)

###### Updates 3/7/2018 
<br> 解决因为网络问题代码中断问题 Adding solutions for disconnect conditions

###### Updates 3/8/2018
<br> 1.fixed a bug in bfx.py
<br> 2.*Changed the data storage from csv to SQL server database.Better for further machine learning process.
