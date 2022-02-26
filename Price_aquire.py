import websocket
import json
import pandas as pd


cc = 'dogeusd'
interval = '1m'
socket = f'wss://stream.binance.com:9443/ws/{cc}t@kline_{interval}'

closes, highs, lows = [], [], []
last_price = []

last_price = closes[-1]


def on_close(ws):
    pass


def on_message(ws, message):
    json_message = json.loads(message)
    cs = json_message['k']

    candle_closed, close, high, low = cs['x'], cs['c'], cs['h'], cs['l']


    if candle_closed:
        closes.append(float(close))
        highs.append(float(high))
        lows.append(float(low))
        last_price.append(float(close))
        price_array = [{close}, {high}, {low}]
        print(f'Current price array: {price_array}')
        df = pd.DataFrame(price_array, index=['close', 'high', 'low'])
        print(df)


ws = websocket.WebSocketApp(socket, on_message=on_message)

ws.run_forever()

