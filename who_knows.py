import websocket
import json
import numpy as np

cc = 'btcusd'
interval = '1m'

socket = f'wss://stream.binance.com:9443/ws/{cc}t@kline_{interval}'

# Trading Strategy Parameters
aroon_time_period = 14

amount = 1000
core_trade_amount = amount*0.80
core_quantity = 0
trade_amount = amount*0.20
core_to_trade = True

portfolio = 0
investment, real_time_portfolio_value, closes, highs, lows = [], [], [], [], []
money_end = amount

# Buying and Selling functions

def buy(allocated_money, price):
  global portfolio, money_end
  quantity = allocated_money/price
  money_end -= quantity*price
  portfolio += quantity
  if investment == []:
    investment.append(allocated_money)
  else:
    investment.append(allocated_money)
    investment[-1] += investment[-2]

def sell(allocated_money, price):
  global money_end, portfolio
  quantity = allocated_money / price
  money_end += allocated_money
  portfolio -= quantity
  investment.append(-allocated_money)
  investment[-1] += investment[-2]