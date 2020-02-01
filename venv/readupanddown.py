
import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib as mpl

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2020, 1, 17)

df = web.DataReader("BBRI.JK", 'yahoo', start, end)
close_px = df['Adj Close']

rets = close_px / close_px.shift(1) - 1
rets.plot(label='return')
plt.show()