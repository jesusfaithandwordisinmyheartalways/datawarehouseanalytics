import pandas as pd

# Extract
df = pd.read_csv('../data/raw/sales.csv')

# Transform
df['total_price'] = df['quantity'] * df['unit_price']

# Load
df.to_csv('../data/processed/sales_clean.csv', index=False)
print("sales_clean.csv created successfully!")