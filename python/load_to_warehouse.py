import pandas as pd
import psycopg2

# Read cleaned data
df = pd.read_csv("../data/processed/sales_clean.csv")

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="sales_dw",
    user="postgres",
    password="Password3!",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Insert into dimensions
for _, row in df.iterrows():

    # Insert customer
    cur.execute("""
        INSERT INTO customer_dim (customer_name, customer_city)
        VALUES (%s, %s)
        ON CONFLICT DO NOTHING
        RETURNING customer_id;
    """, (row["customer_name"], row["customer_city"]))
    customer_id = cur.fetchone()[0] if cur.rowcount > 0 else None

    # Insert product
    cur.execute("""
        INSERT INTO product_dim (product_name, category)
        VALUES (%s, %s)
        ON CONFLICT DO NOTHING
        RETURNING product_id;
    """, (row["product_name"], row["category"]))
    product_id = cur.fetchone()[0] if cur.rowcount > 0 else None

    # Insert date
    cur.execute("""
        INSERT INTO date_dim (full_date, year, month, day)
        VALUES (%s, %s, %s, %s)
        RETURNING date_id;
    """, (row["date"],
          pd.to_datetime(row["date"]).year,
          pd.to_datetime(row["date"]).month,
          pd.to_datetime(row["date"]).day))
    date_id = cur.fetchone()[0]

    # Insert fact row
    cur.execute("""
        INSERT INTO sales_fact (date_id, customer_id, product_id, quantity, unit_price, total_price)
        VALUES (%s, %s, %s, %s, %s, %s);
    """, (date_id, customer_id, product_id,
          row["quantity"], row["unit_price"], row["total_price"]))

# Save + close
conn.commit()
cur.close()
conn.close()

print("Data successfully loaded into warehouse!")