import datetime #library to get time, including the current time
import pandas_datareader.data as web
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib as mpl
import matplotlib.collections as collections
import numpy as np
import re


#print(plt.style.available)
# check available stye

stockCodeInp = input("Please enter a stock ticker code: ")
stockCode = stockCodeInp.upper()
while not re.match("^[A-Z:\\.0-9]+$", stockCode):
    stockCode = input("Please input a correct stock symbol:")



startDate = datetime.datetime(2010, 1, 1)
endDate = datetime.date.today()
df = web.DataReader(stockCode, 'yahoo', startDate, endDate)
df.tail(-5)






close_pr = df['Adj Close'] #Adjusted closing price as a parameter
sma5 = close_pr.rolling(window=5).mean()
sma20 = close_pr.rolling(window=20).mean()
sma100 = close_pr.rolling(window=100).mean()
sma200 = close_pr.rolling(window=200).mean()

diff = sma100 < sma200
diffForward = diff.shift(1)
crossing = np.where(abs(diff - diffForward) == 1)[0]

print(df.iloc[crossing])

mpl.rc('figure', figsize=(9, 7))
mpl.__version__


# Adjusting the style of matplotlib
#plt.style.use('seaborn-dark-palette')
style.use('ggplot')


ax1 = plt.subplot2grid((6,1),(0,0), rowspan=5, colspan=7)
close_pr.plot(label='Daily', linestyle='--', linewidth="0.5")
#sma5.plot(label='SMA5')
sma20.plot(label='SMA20')
sma100.plot(label='SMA100')
sma200.plot(label='SMA200')
plt.legend()
#we put label in each plots argument instead of at the plt.legend
#to make our code more self-documented


ax1.set_title(str(stockCode) + ' Simple Moving Average Graph')

ax2 = plt.subplot2grid((6,1),(5,0), rowspan=1, colspan=1, sharex=ax1)
ax2.bar(df.index, df['Volume'])
plt.legend()

plt.tight_layout()

plt.subplots_adjust(hspace=1.5)
plt.grid(True)

#plt.savefig(str(stockCode)+'_SMAGraph'.png)


plt.show()
