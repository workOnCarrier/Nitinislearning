# https://medium.com/quant-factory/chatgpt-trading-strategy-fully-backtested-with-python-70e6769ab550
# https://www.youtube.com/watch?v=gdjuH4InlL4
# download test data -- https://www.quantfactory.ai/p/tesla-hourly-data

import datetime as dt

import pandas as pd
import numpy as np
import pandas_ta


tsla_prices_df = pd.read_csv('tsla_1h_prices.csv')

# calculate VWAP indicateor and then first strategy signal

tsla_prices_df['typical_price'] = (tsla_prices_df['high']+tsla_prices_df['low']+tsla_prices_df['close'])/3

tsla_prices_df['typical_price_volume'] = tsla_prices_df['typical_price']*tsla_prices_df['volume']

tsla_prices_df['cumm_price_volume'] = tsla_prices_df['typical_price_volume'].rolling(20).sum()

tsla_prices_df['cumm_volume'] = tsla_prices_df['volume'].rolling(20).sum()

tsla_prices_df['vwap'] = tsla_prices_df['cumm_price_volume']/tsla_prices_df['cumm_volume']

tsla_prices_df


# close VWAP cross over signal

tsla_prices_df['close_lag_1'] = tsla_prices_df['close'].shift()

tsla_prices_df['vwap_lag_1'] = tsla_prices_df['vwap'].shift()

tsla_prices_df['signal_1'] = tsla_prices_df.apply(lambda x: 1 if (x['close_lag_1']<x['vwap_lag_1'])&
                                                               (x['close']>x['vwap'])
                                               else (-1 if (x['close_lag_1']>x['vwap_lag_1'])&
                                                           (x['close']<x['vwap']) else np.nan),
                                               axis=1)


# improve strategy by adding RSI cross over condirtion -- above and below 50

tsla_prices_df['rsi'] = pandas_ta.rsi(close=tsla_prices_df['close'],
                                      length=20)

tsla_prices_df['rsi_lag_1'] = tsla_prices_df['rsi'].shift()

tsla_prices_df['signal_2'] = tsla_prices_df.apply(lambda x: 1 if (x['rsi']>50) & (x['rsi_lag_1']<50)
                                               else (-1 if (x['rsi']<50) & (x['rsi_lag_1']>50) else np.nan),
                                               axis=1)


tsla_prices_df[['close', 'vwap']].plot(figsize=(16,4), lw=2)

tsla_prices_df.apply(lambda x: x['open'] if (x['signal_1']==1)&(x['signal_2']==1)
                     else np.nan, axis=1).plot(marker='^',
                                              color='green',
                                              ms=10)
tsla_prices_df.apply(lambda x: x['close'] if (x['signal_1']==-1)*(x['signal_2']==-1)
                     else np.nan, axis=1).plot(marker='v',
                                               color='red',
                                               ms=10)

plt.title('TSLA Stock Price')

plt.show()