from portfolio_class_def import Portfolio
import pandas as pd
import ccxt
import pandas_ta as ta
# 1. Packages for pandas, portfolio_class_def, and ccxt are required.


# 2. Initialize portfolio
beta, delta = [], []
# 3. Beta and delta are our cash to invest, and holding amount respectively
# 4. In order to keep track of our spending and selling history, we use an array
beta.append(input("How much money do we have to  start to invest?"))
delta.append(input("How much crypto do we currently have?"))
alpha = Portfolio(cash_to_invest=beta[-1], holding_amt=delta[-1])
# 5. This is a portfolio class created by Lord Grim imported in (above)

# 6. A while loop to keep the program running until you end it
while alpha:

    exchange = ccxt.binanceus()
    markets = exchange.fetch_ohlcv('DOGE/USD', '1m', limit=28)
# 7. we call our data from our exchange, noting our currency, timeframe, and how many data points
    last_price = [] # 8. create an array to house our data, each point is a package that consists of time, open, high, low, close, and volume
    dragon = markets[27]  # 9. Take the latest data point an put it into another array
    last_price = dragon[4]  # 10. This gets our closing price to do our trades
    print(f'The last price was ${last_price} USD')
    # TA Portion using pandas ta
    tframe = pd.DataFrame(data=markets, columns=['time', 'O', 'H', 'L', 'C', 'V'])
    rsi_frame = ta.rsi(close=tframe['C'], talib=None, length=14)
    adx_data = ta.adx(high=tframe['H'], close=tframe['C'], low=tframe['L'], length=14)
    adx_frame = pd.DataFrame(data=adx_data)
    print(adx_frame)
    tframe['RSI'] = rsi_frame
    tframe['ADX'] = adx_data.iloc[:, 0]
    tframe['DMP'] = adx_data.iloc[:, 1]
    tframe['DMN'] = adx_data.iloc[:, 2]
    print(tframe)
    # print(adx_data) these are the original data pacakges/frames test these to see if the new frame has true values
    # print(adx_frame)
    buy_or_sell = (int(input("Would you like to buy:0 or sell:1?")))
# 11. Simple loop for buying and selling
    if buy_or_sell == 0:
        alpha.buy_asset(invest_amt=float(input("How much should we invest?")), asset_price=float(last_price))
        portfolio_array = [alpha.cash_to_invest, alpha.holding_amt]
        df = pd.DataFrame(portfolio_array, index=['Money to invest', 'Discrete asset quantity'])
        print(df)
    elif buy_or_sell == 1:
        alpha.sell_asset(sell_amt=float(input("How much should we sell?")), asset_price=float(last_price))
        portfolio_array = [alpha.cash_to_invest, alpha.holding_amt]
        df = pd.DataFrame(portfolio_array, index=['Money to invest', 'Discrete asset quantity'])
        print(df)
    else:
        print("Pick a valid value Shit Lord")
        portfolio_array = [alpha.cash_to_invest, alpha.holding_amt]
        df = pd.DataFrame(portfolio_array, index=['Money to invest', 'Discrete asset quantity'])
        print(df)


