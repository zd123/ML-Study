import pandas as pd
import numpy as np
df = pd.read_csv('correlation_example_data.csv')

""" CORRELATION 
https://www.youtube.com/watch?v=DVQ1kA1Mj_w
r = (1 / N - 1) * (sum(XY)  - N * X.mean() * Y.mean() )
 ( divided by )
 std(X) * std(Y)
"""

# print df.head()
X = df['X']
Y = df['Y'] 
N = len(df)
one =  (  1. / (N - 1 ) )
two = (X * Y).sum()
three = (N * (X.mean() * Y.mean()) )
four = X.std() * Y.std()
print one, two, three, four

r = one * (two - three)  / four
print r 

df['XX'] = df['X']**4
print df.head(1)
print df.corr()