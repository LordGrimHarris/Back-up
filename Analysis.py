import pandas as pd
import ccxt
import pandas_ta as ta
import statistics

frame = pd.DataFrame(columns = ['High'])

exchange = ccxt.binanceus()

cc = ('dogeusd').upper()
kline = '1m'
points = 1000

markets = exchange.fetch_ohlcv(cc, kline, limit = points)

c_frame = pd.DataFrame(data = markets, columns = ['time', 'O', 'H', 'L', 'C', 'V'])

alpha = pd.DataFrame(data = markets)
beta = pd.DataFrame(data = [])
beta.append(c_frame['C'].max())
print(frame)
print(alpha)

