# Bitcoin Trade Data
## The goal for this project is to get bitcoin related data to predict bitcoin price.

#### The related data including:
<br> quarterly and weekly bitcoin price from OKEX
<br> asks/bids info and last price from Bitfinex (Will add funding data later)
<br> USDT OTC price from Huobi.pro
<br> Emotion from news and forum (Wallstreet.cn and 8btc , will add reddit and CCN later)(DELETED due to effeciency reason)

After the data prediction, will start another project to autotrade the future in OKex thru machine learning result.

### run input_data.py

需要提前安装
You need to install below packages before run input_data.py
<br>`pip install requests` -- Access to webpage
<br>`pip install BeautifulSoup` -- Formalize webpage
<br>`pip install snownlp` -- Analyze emotion of sentenses in Chinese
<br>`pip install pyodbc` -- connect to SQL Server DB

 Will update the code from time to time.

<br> ------------------------------------------------------------------------------

# Updates by Date

###### Updates 3/6/2018 
<br> 1. get the news from wallstreet cn(https://wallstreetcn.com/) blockchain channel. Analyze the emotion thru SnowNLP. Input as a feature.
<br> 2. get the posts from Chinese biggest BTC forum--8btc cn(https://8btc.com/) blockchain channel. Analyze the emotion by using SnowNLP. Input as a feature.
(Will Update and input the emotion from Reddit and CCN in the future)

###### Updates 3/7/2018 
<br>  Adding solutions for disconnect conditions

###### Updates 3/8/2018
<br> 1.fixed a bug in bfx.py
<br> 2.*Changed the data storage from csv to SQL server database.Better for further machine learning process.

###### Updates 3/10/2018
<br> Start another project named Bitcoin_price_prediction to predict bitcoin trend.

###### Updates 3/14/2018
<br> DELETED Emotion from forum due to effeciency reason
