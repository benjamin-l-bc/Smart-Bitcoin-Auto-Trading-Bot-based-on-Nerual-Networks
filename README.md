# Bitcoin Trade Data
## The goal for this project is 1)to get bitcoin related data to predict bitcoin price. 2)Predict Bitcoin future price 3)Auto-trading based on the prediction(Long Only)

#### The related data including:
<br> quarterly and weekly bitcoin price from OKEX
<br> asks/bids info and last price from Bitfinex (Will add funding data later)
<br> USDT OTC price from Huobi.pro
<br> Emotion from news and forum (Wallstreet.cn and 8btc , will add reddit and CCN later)(DELETED due to effeciency reason)

#### Outcomes:
3 predicted outcomes: Next_5,Next_10,Next_15 refer to the bitcoin future price will raise or drop in next 5/10/15 minutes based on our prediction 

#### Machine Learning Model:
<br> Neural Network

### Steps
#### 1) run input_data.py to collect data to SQL Database.
#### 2) https://github.com/benjaminshi02003220/Bitcoin_price_prediction Download this project and run NNC.py to build up the model based on  the data in SQL Database
#### 3) Copy the 4 model file from Bitcoin_price_prediction folder to bitcion_trade_data folder. Run prediction.py to 1.predict price 2.Auto-Trading based on the result(To be completed)


You need to install below packages before run input_data.py
<br>`pip install requests` -- Access to webpage
<br>`pip install BeautifulSoup` -- Formalize webpage
<br>`pip install snownlp` -- Analyze emotion of sentenses in Chinese
<br>`pip install pyodbc` -- connect to SQL Server DB
<br>`pip install sklearn` -- Machine Learning Model

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

###### Updates 3/14/2018
<br>adding prediction.py (To be Updated)

###### Updates 3/18/2018
<br>Fixed some bugs and complete the real-time prediction. (prediction.py). Next step is to accomplish the auto-trading based on the prediction result~ 

###### Updates 3/28/2018
<br>3 predicted outcomes: Next_5,Next_10,Next_15 refer to the bitcoin future price will raise or drop based on our prediction , 1 means raise ,0 means drop. If two of the three outcomes are 1, we can long bitcoin future and will sell it after 15 minutes/or a certain percentage of profit(to be tested)

###### Updates 4/4/2018
<br>Adding future trading process
