import pandas as pd

df = pd.read_csv('../data/processed/sales_clean.csv')

df['month'] = pd.to_datetime(df['date']).dt.month
df['year'] = pd.to_datetime(df['date']).dt.year

df.to_csv('../data/processed/sales_features.csv', index=False)
print("Feature dataset created successfully!")