import statsmodels.api as sm
import statsmodels.formula.api as smf

import pandas as pd
df = pd.read_csv('data/housing-data.csv')
df['constant'] = 1
df.head()

y = df['price']
X = df[['sqft', 'bdrms', 'age', 'constant']]

algo = sm.OLS(y, X)
residuals = algo.fit()
residuals.summary()




