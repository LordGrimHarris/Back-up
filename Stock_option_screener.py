from yahoo_fin import options
import pandas as pd

stock = 'CCL'
pd.set_option('display.max_columns', None)
chain = options.get_options_chain(stock)
print(chain)