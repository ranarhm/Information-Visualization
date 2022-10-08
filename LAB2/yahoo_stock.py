import pandas_datareader as web
import pandas as pd
from prettytable import PrettyTable

stocks = ["AAPL", "ORCL", "TSLA", "IBM", "YELP", "MSFT"]
df = web.DataReader(stocks[0], data_source="yahoo", start="2000-01-01",
                    end="2022-09-01")

# create an empty dataframe to fill with data
df1 = pd.DataFrame(index=stocks, columns=df.columns)

# mean
df2 = df1.copy()
for i in range(len(stocks)):
    df2.iloc[i] = web.DataReader(stocks[i], data_source="yahoo", start="2000-01-01",
                                 end="2022-09-01").mean().round(2)

df2.loc['Maximum value'] = df2.max().values
df2.loc['Minimum value'] = df2.min().values
df2.loc['Maximum company'] = df2.astype(float).idxmax().values
df2.loc['Minimum company'] = df2.iloc[:6].astype(float).idxmin().values

x = PrettyTable()
x.title = 'Mean Value Comparison'
row_index = list(df2.index.values)
x.field_names = ['', 'High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close']
for i in range(len(row_index)):
    new_list = df2.iloc[i].values.tolist()
    new_list.insert(0, row_index[i])
    x.add_row(new_list)
print(x)

# variance
df3 = df1.copy()
for i in range(len(stocks)):
    df3.iloc[i] = web.DataReader(stocks[i], data_source="yahoo", start="2000-01-01",
                                 end="2022-09-01").var().round(2)

df3.loc['Maximum value'] = df3.max().values
df3.loc['Minimum value'] = df3.min().values
df3.loc['Maximum company'] = df3.astype(float).idxmax().values
df3.loc['Minimum company'] = df3.iloc[:6].astype(float).idxmin().values

x.clear_rows()
x.title = 'Variance Value Comparison'
x.field_names = ['', 'High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close']
for i in range(len(row_index)):
    new_list = df3.iloc[i].values.tolist()
    new_list.insert(0, row_index[i])
    x.add_row(new_list)
print(x)

# std
df4 = df1.copy()
for i in range(len(stocks)):
    df4.iloc[i] = web.DataReader(stocks[i], data_source="yahoo", start="2000-01-01",
                                 end="2022-09-01").std().round(2)

df4.loc['Maximum value'] = df4.max().values
df4.loc['Minimum value'] = df4.min().values
df4.loc['Maximum company'] = df4.astype(float).idxmax().values
df4.loc['Minimum company'] = df3.iloc[:6].astype(float).idxmin().values

x.clear_rows()
x.field_names = ['', 'High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close']
x.title = 'Standard Deviation Value Comparison'
for i in range(len(row_index)):
    new_list = df4.iloc[i].values.tolist()
    new_list.insert(0, row_index[i])
    x.add_row(new_list)
print(x)

# median
df5 = df1.copy()
for i in range(len(stocks)):
    df5.iloc[i] = web.DataReader(stocks[i], data_source="yahoo", start="2000-01-01",
                                 end="2022-09-01").median().round(2)

df5.loc['Maximum value'] = df5.max().values
df5.loc['Minimum value'] = df5.min().values
df5.loc['Maximum company'] = df5.astype(float).idxmax().values
df5.loc['Minimum company'] = df5.iloc[:6].astype(float).idxmin().values

x.clear_rows()
x.field_names = ['', 'High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close']
x.title = 'Median Value Comparison'
for i in range(len(row_index)):
    new_list = df5.iloc[i].values.tolist()
    new_list.insert(0, row_index[i])
    x.add_row(new_list)
print(x)

# corr
for i in range(len(stocks)):
    df_corr = web.DataReader(stocks[i], data_source="yahoo", start="2000-01-01",
                        end="2022-09-01")
    print(f'The correlation matrix for the {stocks[i]} company with all the given features is: \n{df_corr.corr().round(2)}')
