# bitcoin_trade_info
## 需要在input_data中输入private_Key和public_Key,然后运行input_data.py
## 目标是用机器学习自动交易okex的bitcoin季度和周的期货合约进行套利。
##### 1. 按照时间60秒间隔抓取OKEX，huobi_USDT,bfx上现货价格。
##### 2. 用sklearn进行机器学习找出最佳策略最大化收益。
##### 3. 用okex API进行自动交易。

代码尚未完成并会不断进行完善~

###### 3/6/2018 更新 
1.从华尔街见闻的区块链频道抓取新闻，使用SnowNLP分析新闻的情绪，news_emotion作为最后分析的feature
2.从8btc论坛抓取新闻，使用SnowNLP分析论坛帖子和回帖的情绪，8btc_emotion作为最后分析的feature
