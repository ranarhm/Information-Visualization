import pandas_datareader as web
from tabulate import tabulate
import pandas as pd

stocks = ["AAPL", "ORCL", "TSLA", "IBM", "YELP", "MSFT"]
df_appl = web.DataReader(stocks[0], data_source="yahoo", start="2000-01-01", end="2022-09-13")
df_orcl = web.DataReader(stocks[1], data_source="yahoo", start="2000-01-01", end="2022-09-13")
df_tsla = web.DataReader(stocks[2], data_source="yahoo", start="2000-01-01", end="2022-09-13")
df_ibm = web.DataReader(stocks[3], data_source="yahoo", start="2000-01-01", end="2022-09-13")
df_yelp = web.DataReader(stocks[4], data_source="yahoo", start="2000-01-01", end="2022-09-13")
df_msft = web.DataReader(stocks[5], data_source="yahoo", start="2000-01-01", end="2022-09-13")

columns = list(["Name\Feature", "High($)", "Low($)", "Open($)", "Close($)", "Volume", "Adj Close($)"])

data_mean = [
    ["\'AAPL\'", df_appl['High'].mean(), df_appl['Low'].mean(), df_appl['Open'].mean(), df_appl['Close'].mean(),
     df_appl['Volume'].mean(), df_appl['Adj Close'].mean()],
    ["\'ORCL\'", df_orcl['High'].mean(), df_orcl['Low'].mean(), df_orcl['Open'].mean(), df_orcl['Close'].mean(),
     df_orcl['Volume'].mean(), df_orcl['Adj Close'].mean()],
    ["\'TSLA\'", df_tsla['High'].mean(), df_tsla['Low'].mean(), df_tsla['Open'].mean(), df_tsla['Close'].mean(),
     df_tsla['Volume'].mean(), df_tsla['Adj Close'].mean()],
    ["\'IBM\'", df_ibm['High'].mean(), df_ibm['Low'].mean(), df_ibm['Open'].mean(), df_ibm['Close'].mean(),
     df_ibm['Volume'].mean(), df_ibm['Adj Close'].mean()],
    ["\'YELP\'", df_yelp['High'].mean(), df_yelp['Low'].mean(), df_yelp['Open'].mean(), df_yelp['Close'].mean(),
     df_yelp['Volume'].mean(), df_yelp['Adj Close'].mean()],
    ["\'MSFT\'", df_msft['High'].mean(), df_msft['Low'].mean(), df_msft['Open'].mean(), df_msft['Close'].mean(),
     df_msft['Volume'].mean(), df_msft['Adj Close'].mean()]
]
df = pd.DataFrame(data_mean, columns=columns)
col = df.columns
for i in range(1, 7):
    df[col[i]] = df[col[i]].astype('float64')


def max_value(i):
    return df.loc[df[col[i]].idxmax(), col[0]]


def min_value(i):
    return df.loc[(df[col[i]].str.isalpha() != True).idxmin(), col[0]]


df.loc[len(df.index)] = ['Maximum Value', max_value(1), max_value(2), max_value(3), max_value(4), max_value(5),
                         max_value(6)]
df.loc[len(df.index)] = ['Minimum Value', min_value(1), min_value(2), min_value(3), min_value(4), min_value(5),
                         min_value(6)]
print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))


data_var = [
    ["\'AAPL\'", df_appl['High'].var(), df_appl['Low'].var(), df_appl['Open'].var(), df_appl['Close'].var(),
     df_appl['Volume'].var(), df_appl['Adj Close'].var()],
    ["\'ORCL\'", df_orcl['High'].var(), df_orcl['Low'].var(), df_orcl['Open'].var(), df_orcl['Close'].var(),
     df_orcl['Volume'].var(), df_orcl['Adj Close'].var()],
    ["\'TSLA\'", df_tsla['High'].var(), df_tsla['Low'].var(), df_tsla['Open'].var(), df_tsla['Close'].var(),
     df_tsla['Volume'].var(), df_tsla['Adj Close'].var()],
    ["\'IBM\'", df_ibm['High'].var(), df_ibm['Low'].var(), df_ibm['Open'].var(), df_ibm['Close'].var(),
     df_ibm['Volume'].var(), df_ibm['Adj Close'].var()],
    ["\'YELP\'", df_yelp['High'].var(), df_yelp['Low'].var(), df_yelp['Open'].var(), df_yelp['Close'].var(),
     df_yelp['Volume'].var(), df_yelp['Adj Close'].var()],
    ["\'MSFT\'", df_msft['High'].var(), df_msft['Low'].var(), df_msft['Open'].var(), df_msft['Close'].var(),
     df_msft['Volume'].var(), df_msft['Adj Close'].var()]
]
df = pd.DataFrame(data_var, columns=columns)
df.loc[len(df.index)] = ['Maximum Value', max_value(1), max_value(2), max_value(3), max_value(4), max_value(5),
                         max_value(6)]
df.loc[len(df.index)] = ['Minimum Value', min_value(1), min_value(2), min_value(3), min_value(4), min_value(5),
                         min_value(6)]
print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))


data_std = [
    ["\'AAPL\'", df_appl['High'].std(), df_appl['Low'].std(), df_appl['Open'].std(), df_appl['Close'].std(),
     df_appl['Volume'].std(), df_appl['Adj Close'].std()],
    ["\'ORCL\'", df_orcl['High'].std(), df_orcl['Low'].std(), df_orcl['Open'].std(), df_orcl['Close'].std(),
     df_orcl['Volume'].std(), df_orcl['Adj Close'].std()],
    ["\'TSLA\'", df_tsla['High'].std(), df_tsla['Low'].std(), df_tsla['Open'].std(), df_tsla['Close'].std(),
     df_tsla['Volume'].std(), df_tsla['Adj Close'].std()],
    ["\'IBM\'", df_ibm['High'].std(), df_ibm['Low'].std(), df_ibm['Open'].std(), df_ibm['Close'].std(),
     df_ibm['Volume'].std(), df_ibm['Adj Close'].std()],
    ["\'YELP\'", df_yelp['High'].std(), df_yelp['Low'].std(), df_yelp['Open'].std(), df_yelp['Close'].std(),
     df_yelp['Volume'].std(), df_yelp['Adj Close'].std()],
    ["\'MSFT\'", df_msft['High'].std(), df_msft['Low'].std(), df_msft['Open'].std(), df_msft['Close'].std(),
     df_msft['Volume'].std(), df_msft['Adj Close'].std()]
]
df = pd.DataFrame(data_std, columns=columns)
df.loc[len(df.index)] = ['Maximum Value', max_value(1), max_value(2), max_value(3), max_value(4), max_value(5),
                         max_value(6)]
df.loc[len(df.index)] = ['Minimum Value', min_value(1), min_value(2), min_value(3), min_value(4), min_value(5),
                         min_value(6)]
print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))


data_median = [
    ["\'AAPL\'", df_appl['High'].mean(), df_appl['Low'].mean(), df_appl['Open'].mean(), df_appl['Close'].mean(),
     df_appl['Volume'].mean(), df_appl['Adj Close'].mean()],
    ["\'ORCL\'", df_orcl['High'].mean(), df_orcl['Low'].mean(), df_orcl['Open'].mean(), df_orcl['Close'].mean(),
     df_orcl['Volume'].mean(), df_orcl['Adj Close'].mean()],
    ["\'TSLA\'", df_tsla['High'].mean(), df_tsla['Low'].mean(), df_tsla['Open'].mean(), df_tsla['Close'].mean(),
     df_tsla['Volume'].mean(), df_tsla['Adj Close'].mean()],
    ["\'IBM\'", df_ibm['High'].mean(), df_ibm['Low'].mean(), df_ibm['Open'].mean(), df_ibm['Close'].mean(),
     df_ibm['Volume'].mean(), df_ibm['Adj Close'].mean()],
    ["\'YELP\'", df_yelp['High'].mean(), df_yelp['Low'].mean(), df_yelp['Open'].mean(), df_yelp['Close'].mean(),
     df_yelp['Volume'].mean(), df_yelp['Adj Close'].mean()],
    ["\'MSFT\'", df_msft['High'].mean(), df_msft['Low'].mean(), df_msft['Open'].mean(), df_msft['Close'].mean(),
     df_msft['Volume'].mean(), df_msft['Adj Close'].mean()]
]
df = pd.DataFrame(data_median, columns=columns)
df.loc[len(df.index)] = ['Maximum Value', max_value(1), max_value(2), max_value(3), max_value(4), max_value(5),
                         max_value(6)]
df.loc[len(df.index)] = ['Minimum Value', min_value(1), min_value(2), min_value(3), min_value(4), min_value(5),
                         min_value(6)]
print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))


print(f'The correlation matrix for the Apple company with all the given features is: \n{df_appl.corr()}')
print(f'The correlation matrix for the Oracle company with all the given features is: \n{df_orcl.corr()}')
print(f'The correlation matrix for the Tesla company with all the given features is: \n{df_tsla.corr()}')
print(f'The correlation matrix for the IBM company with all the given features is: \n{df_ibm.corr()}')
print(f'The correlation matrix for the Yelp company with all the given features is: \n{df_yelp.corr()}')
print(f'The correlation matrix for the Microsoft company with all the given features is: \n{df_msft.corr()}')


