from sklearn.linear_model import LinearRegression
import pandas as pd

df = pd.read_csv('../data/processed/sales_clean.csv')

X = df[['quantity', 'unit_price']]   # FIXED error here
y = df['total_price']

model = LinearRegression()
model.fit(X, y)

print("Baseline coefficients:", model.coef_)
print("Intercept:", model.intercept_)