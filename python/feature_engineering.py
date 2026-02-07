import pandas as pd

df = pd.read_csv('data/processed/sales_clean.csv')

df['order_date'] = pd.to_datetime(df['order_date'])
df['dispatch_date'] = pd.to_datetime(df['dispatch_date'])
df['month'] = df['order_date'].dt.month_name().str[:3]  # Abbreviation Jan, Feb, etc.
df['year'] = df['order_date'].dt.year

df['region'] = df['region'].fillna('Unknown')

# Optional aggregations for Tableau
df['total_customers'] = df['customer_name'].nunique()
df['total_profit'] = df['profit']
df['total_sales'] = df['total_sales']

# Save CSV + Excel
df.to_csv('data/processed/sales_features.csv', index=False)
df.to_excel('data/processed/sales_features.xlsx', index=False)

print("sales_features.csv and sales_features.xlsx with month abbreviation and totals created successfully!")