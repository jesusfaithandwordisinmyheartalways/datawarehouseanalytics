-- DIMENSION TABLES
CREATE TABLE product_dim (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50)
);

CREATE TABLE customer_dim (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100),
    customer_city VARCHAR(100)
);

CREATE TABLE date_dim (
    date_id SERIAL PRIMARY KEY,
    full_date DATE,
    year INT,
    month INT,
    day INT
);

-- FACT TABLE
CREATE TABLE sales_fact (
    sale_id SERIAL PRIMARY KEY,
    date_id INT REFERENCES date_dim(date_id),
    customer_id INT REFERENCES customer_dim(customer_id),
    product_id INT REFERENCES product_dim(product_id),
    quantity INT,
    unit_price NUMERIC(10,2),
    total_price NUMERIC(10,2)
);