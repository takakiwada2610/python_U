# データ解析のセクション
"""
import numpy as np

a = np.array([[1, 2, 3],[4, 5, 6]])
print(a)
print(a[1])
print(a[0][0])

s = a.shape
n = a.ndim
d = a.dtype.name
ss = a.size
print(s,n,d,ss)

arange = np.arange(0, 30, 5)
zeros = np.zeros((3, 4))
line = np.linspace(0, 2, 9)
print(arange)
print(zeros)
print(line)

aa = np.arange(6).reshape(2, 3)
aaa = np.arange(24).reshape(2, 3, 4)
print(aa)
print(aaa)

x = np.arange(0, 10, 2)
y = np.arange(5)
z = np.arange(0, 100, 20)

print(np.append(x, y))
print(np.vstack([x, y, z]))
print(np.hstack([x, y, z]))

a = np.array([10, 20, 30, 40, 50])
b = np.arange(5)
print(a-b)
print(b-a)
print(a < 30)
print(a*3)

a = np.random.random((2, 3))
sum = a.sum()
min = a.min()
max = a.max
print(a)
print(sum, min)

a = np.arange(12).reshape(3, 4)
axis0 = a.sum(axis=0)
axis1 = a.sum(axis=1)
print(a)
print(axis0, axis1)
print(a.T)

import numpy as np
import matplotlib.pyplot as plt

v = np.random.normal(2, 0.5, 10000)

plt.hist(v, bins=50, density=1)
plt.show()
"""

##########################################################
# pandasの練習
import numpy as np
import pandas as pd

s = pd.Series([1, 2, np.nan])
print(s)
print(s[0])
print(s.sum())

df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
print(df)

df = pd.DataFrame(np.random.randn(6, 4))
print(df)
df = pd.DataFrame(np.random.randn(6, 4), index=pd.date_range('20170101', periods=6))
print(df)
df = pd.DataFrame(np.random.randn(6, 4), index=pd.date_range('20170101', periods=6), columns=['A', 'B', 'C', 'D'])
print(df)
print(df.head(1))
print(df.describe())
print(df.T)

import pandas_datareader
s = pandas_datareader.data.DataReader('AAPL', 'yahoo', '2014-01-01')
print(s)


# matplotlibの使い方
