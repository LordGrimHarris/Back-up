import ccxt
import pandas as pd
import pandas_ta as ta
from portfolio_class_def import *  # (important class that can be copied at eh top before (#1) or you can download the file to your python path/project)
import numpy as np
import array
import matplotlib.pyplot as plt

# 1. Call financial data from binance us (because USD)
exchange = ccxt.binanceus()
# 2. This records our OHLCV (Open, High, Low, Close, Volume) data. 'currency', 'kline stick frame', 'number of data points'

# choose your currency
currency = str(input('What would you like to buy and sell today? Remember it has to be a buying pair for crypto')).upper()
# pick your Kline time frame
kline_sticks = str(input("Pick a timeframe: 1m, 5m, 1h, 1M etc"))
data_points = 1000

markets = exchange.fetch_ohlcv(currency, kline_sticks, limit = data_points)
# 3. Puts the data into a data frame
tframe = pd.DataFrame(data = markets, columns = ['time', 'O', 'H', 'L', 'C', 'V'])
# 4. Specific closing prices
caesar = tframe['C']
# 5. Refactor RSI column into dataframe

tframe['RSI'] = ta.rsi(close = tframe['C'], talib = None, length = 14)
currency_x_axis = np.arange(0, data_points)
currency_y_axis = caesar
price_graph = plt.subplot(1, 2, 1)
price_graph.set_title(f'{currency}, price graph')
plt.plot(currency_x_axis, currency_y_axis)

ta_x_axis = np.arange(0, data_points)
ta_y_axis = tframe['RSI']

rsi_graph = plt.subplot(1, 2, 2)
rsi_graph.set_title(f'{currency}, RSI graph')
plt.plot(ta_x_axis, ta_y_axis)
plt.show()