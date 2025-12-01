## Tableau Dashboards

# DataWarehouseAnalytics: Sales Data Warehouse Project

## Project Overview
This project demonstrates building a **mini data warehouse** and creating **business insights dashboards** using real sales data. It covers the full workflow from raw data extraction to clean datasets, star schema modeling, and interactive dashboards.  
The goal is to showcase skills in **data engineering, analytics, and visualization** for a data analyst portfolio.

---



## Technologies & Libraries Used
- **Python**: pandas, scikit-learn, psycopg2  
- **R**: beginner tasks and visualization  
- **PostgreSQL & pgAdmin**: database design, star schema, ETL load  
- **Tableau**: interactive dashboards & data visualization  
- **Power BI Service**: cloud dashboards, interactive visualizations  
- **Airflow** *(optional)*: ETL workflow automation  

---

## Key Steps in the Project
1. **Data Cleaning & ETL**  
   - Raw CSV data (`sales.csv`) cleaned using Python and saved as `sales_clean.csv`.  
   - Added derived columns (`total_price`, `month`, `year`) for analysis.

2. **Star Schema in PostgreSQL**  
   - Created dimension tables (`product_dim`, `customer_dim`, `date_dim`) and fact table (`sales_fact`).  
   - Loaded processed data into PostgreSQL using Python scripts.

3. **Feature Engineering & Baseline Model**  
   - Generated features using Python & R.  
   - Built a simple linear regression baseline to predict total sales.

4. **Data Visualization**  
   - **Tableau**: three dashboards showing sales over time, top products, category distribution, and customer regions.  
   - **Power BI**: similar dashboards created in web-based Power BI Service with interactive filters.

---

## Dashboards Links
### Tableau Dashboards
- [Dashboard 1: Sales Over Time](#)  
- [Dashboard 2: Top Products & Categories](#)  
- [Dashboard 3: Customer Regions](#)  

### Power BI Dashboards
- [Dashboard 1: Sales Insights](#)  
- [Dashboard 2: Product & Category Analysis](#)  
- [Dashboard 3: Customer Insights](#)  









View the interactive dashboards here: [Sales Data Dashboards]
https://public.tableau.com/views/DataWarehouseAnalytics_WorkbookDashboards1/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

https://public.tableau.com/views/DataWarehouseAnalytics_WorkbookDashboards2/Dashboard2?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link


https://public.tableau.com/views/DataWarehouseAnalytics_WorkbookDashboards3/Dashboard3?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link






