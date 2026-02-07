

View the interactive dashboards here: Datawarehouse Global Analysis

https://public.tableau.com/app/profile/andrew.johnson8782/viz/DatawarehouseGlobalAnalysis/Dashboard?publish=yes




# Data Warehouse Analytics Project

This project demonstrates a **Data Warehouse Analytics pipeline** with synthetic sales data for multiple stores across the globe, designed for interactive visualization in **Tableau**. It includes **ETL (Extract, Transform, Load)**, **feature engineering**, **data warehouse loading**, and a **baseline predictive model**. The dataset spans multiple years (2021–2025) and contains realistic warehouse operations data.



The dataset contains **50 rows of synthetic sales data** across multiple countries, regions, and years (2021–2025). Key columns include:

| Column | Description |
|--------|-------------|
| order_date | Date the order was placed |
| dispatch_date | Date the order was dispatched |
| customer_name | Customer or company name |
| customer_city | City of the customer |
| country | Country of the customer |
| region | Region within country (USA states and other regions globally) |
| product_name | Product sold |
| category | Product category (Electronics, Furniture, Warehouse Equipment, Consumables) |
| quantity | Number of units sold |
| unit_price | Price per unit |
| total_price | `quantity * unit_price` |
| profit | Calculated profit based on category margins |
| total_sales | Same as `total_price` for Tableau KPI filtering |

---

## ⚙️ Python Scripts

### 1. `etl_pipeline.py`
- Reads raw CSV (`data/raw/sales.csv`).
- Calculates `total_price`, `profit`, and `total_sales`.
- Saves cleaned CSV and Excel for Tableau (`sales_clean.csv` / `sales_clean.xlsx`).

### 2. `feature_engineering.py`
- Adds features: month abbreviation (`Jan`, `Feb`, …), year, region.
- Outputs CSV + Excel (`sales_features.csv` / `sales_features.xlsx`) ready for Tableau.
- Includes total metrics: `total_sales`, `total_profit`, `total_customers`.

### 3. `load_to_warehouse.py`
- Loads cleaned sales data into a **PostgreSQL data warehouse** with star schema:
  - `product_dim`
  - `customer_dim`
  - `date_dim`
  - `sales_fact`

### 4. `model_baseline.py`
- Fits a **Linear Regression model** to predict `total_price` based on `quantity` and `unit_price`.

---

## 📊 Tableau Dashboard

The project includes an interactive **Tableau dashboard** built from `sales_clean.xlsx` or `sales_features.xlsx`.  

### Sheets:
1. **KPI** – Displays:
   - Total Sales
   - Total Profit
   - Total Customers  
2. **Sales By Country** – Interactive by country filter  
3. **Sales By Month** – Month abbreviations for easier analysis  
4. **Sales By Product** – Revenue per product category  
5. **Dashboard: Datawarehouse Global Analysis** – Combines all sheets for global sales visualization with public filters  

> Filters are linked across all sheets so users can dynamically analyze sales, profit, and customer metrics across countries, months, products, and regions.

---

## 🏃 How to Run the Project

1. **Activate Python Virtual Environment**
```bash
source venv/bin/activate