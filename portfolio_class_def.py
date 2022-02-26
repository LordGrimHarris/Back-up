import pandas as pd


class Portfolio:

    def __init__(self, cash_to_invest, holding_amt):
        self.cash_to_invest = float(cash_to_invest)
        self.holding_amt = float(holding_amt)

    def buy_asset(self, invest_amt, asset_price):

        self.invest_amt = invest_amt * (0.999)
        if self.cash_to_invest >= invest_amt:
            c_quant = (invest_amt / asset_price) * (0.999)
            self.holding_amt += c_quant
            self.cash_to_invest -= invest_amt

    def sell_asset(self, sell_amt, asset_price):

        self.sell_amt = sell_amt
        if self.holding_amt >= sell_amt and self.holding_amt > 0:
            c_quant = (sell_amt * asset_price) * (0.999)
            self.holding_amt -= sell_amt
            self.cash_to_invest += c_quant




