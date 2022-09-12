import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

num_mean_x = input("Enter a number for mean of statistic number x: ")
num_var_x = input("Enter a number for variance of statistic number x: ")
num_observations_x = input("Enter a positive number for number of observations of statistic number x: ")
num_std_x = np.sqrt(int(num_var_x))
num_mean_y = input("Enter a number for mean of statistic number y: ")
num_var_y = input("Enter a number for variance of statistic number y: ")
num_observations_y = input("Enter a positive number for number of observations of statistic number y: ")
num_std_y = np.sqrt(int(num_var_y))

np.random.seed(123)
x = np.random.normal(int(num_mean_x), int(num_std_x), int(num_observations_x))
y = np.random.normal(int(num_mean_y), int(num_std_y), int(num_observations_y))

mean_x = np.mean(x)
mean_y = np.mean(y)
N_x = int(num_observations_x)
N_y = int(num_observations_y)
var_x = np.sum(np.square(x - mean_x)) / (N_x - 1)
var_y = np.sum(np.square(y - mean_y)) / (N_y - 1)


def cal_corr(x, y):
    cov = np.sum((x - np.mean(x)) * (y - np.mean(y)))
    std_x = np.sum(np.square((x - np.mean(x))))
    std_y = np.sum(np.square((y - np.mean(y))))
    corr_org = cov / np.sqrt(std_x * std_y)
    return corr_org


print(f"The sample mean of random variable x is : {mean_x: .2f}")
print(f"The sample mean of random variable y is : {mean_y: .2f}")
print(f"The sample variance of random variable x is : {var_x: .2f}")
print(f"The sample variance of random variable y is : {var_y: .2f}")
print(f"The sample Pearson’s correlation coefficient between x & y is: {cal_corr(x, y): .2f}")

plt.figure()
plt.plot(x)
plt.plot(y)
plt.title("The line graph of the random variables x and y")
plt.xlabel("observations")
plt.ylabel("random variables x and y")
plt.legend(['x', 'y'])
plt.show()

plt.figure()
plt.title("The histogram plot of the random variables x and y")
plt.xlabel("random variables x and y")
plt.ylabel("observations")
plt.hist(x)
plt.hist(y)
plt.legend(['x', 'y'])
plt.show()

url = "https://raw.githubusercontent.com/rjafari979/CS5764-Information-Visualization/main/tute1.csv"
df = pd.read_csv(url)
print(df)

corr_sales_budget = cal_corr(df["Sales"], df["AdBudget"])
corr_sales_gdp = cal_corr(df["Sales"], df["GDP"])
corr_budget_gdp = cal_corr(df["AdBudget"], df["GDP"])

print(f"The sample Pearson’s correlation coefficient between Sales & AdBudget is: {corr_sales_budget: .2f}")
print(f"The sample Pearson’s correlation coefficient between ales & GDP  is: {corr_sales_gdp: .2f}")
print(f"The sample Pearson’s correlation coefficient between AdBudget & GDP is: {corr_budget_gdp: .2f}")

col = df.columns
df.index = df[col[0]]
plt.figure()
df.plot(title="The line plot of Sales, AdBudget and GDP versus time")
plt.xlabel("time series")
plt.ylabel("Sales, AdBudget and GDP")
plt.legend(['Sales', 'AdBudget', 'GDP'], loc="upper left")
plt.show()

col1 = df.columns
df.index = df[col1[0]]
plt.figure()
df.plot(title="The histogram plot of Sales, AdBudget and GDP versus time", kind='hist')
plt.xlabel("Sales, AdBudget and GDP")
plt.ylabel("frequency")
plt.legend(['Sales', 'AdBudget', 'GDP'], loc="upper right")
plt.show()
