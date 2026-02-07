import pandas as pd
import numpy as np

# -----------------
# SIMULATE DATA (50 ROWS)
# -----------------
data = {
    'order_date': pd.date_range(start='2021-01-01', periods=50, freq='15D'),
    'dispatch_date': pd.date_range(start='2021-01-03', periods=50, freq='15D'),
    'customer_name': [
        'John Doe','Jane Smith','Alice Johnson','Bob Lee','Chris Kim',
        'Acme Corp','LogiTech GmbH','EuroPack SAS','FastShip Ltd','SupplyPro',
        'GlobalStore','Warehouse King','PackRight','StorageHub','LogiMax',
        'DistribCo','QuickMove','ShipRight','ProLogistics','MegaWare',
        'Warehouse Pro','LogisticsPlus','GlobalMove','SupplyChain Inc','FastShip 2',
        'EuroShip','NorthStar','SouthStar','EastPort','WestPort',
        'CentralWare','Alpha Logistics','Beta Logistics','Gamma Storage','Delta Storage',
        'Omega Warehouses','Prime Logistics','Elite Warehouses','Skyline Supply','Horizon Warehouses',
        'MetroLogistics','CityShip','TownShip','RegionalWare','NationalWare',
        'InternationalShip','GlobalExpress','Worldwide Logistics','Universal Supply','Mega Global'
    ],
    'customer_city': [
        'New York','Chicago','Miami','Seattle','Los Angeles','Toronto','Berlin','Paris','London','Cape Town',
        'Amsterdam','Dallas','Madrid','Milan','Vancouver','Nairobi','Houston','Atlanta','Sydney','Melbourne',
        'Boston','San Francisco','Rome','Lisbon','Stockholm','Oslo','Copenhagen','Helsinki','Reykjavik','Zurich',
        'Vienna','Brussels','Warsaw','Prague','Budapest','Athens','Istanbul','Dubai','Mumbai','Tokyo',
        'Beijing','Shanghai','Seoul','Bangkok','Singapore','Mexico City','Buenos Aires','Santiago','Lima','Bogota'
    ],
    'country': [
        'USA','USA','USA','USA','USA','Canada','Germany','France','UK','South Africa',
        'Netherlands','USA','Spain','Italy','Canada','Kenya','USA','USA','Australia','Australia',
        'USA','USA','Italy','Portugal','Sweden','Norway','Denmark','Finland','Iceland','Switzerland',
        'Austria','Belgium','Poland','Czech Republic','Hungary','Greece','Turkey','UAE','India','Japan',
        'China','China','South Korea','Thailand','Singapore','Mexico','Argentina','Chile','Peru','Colombia'
    ],
    'region': [
        'East','Midwest','South','West','West','Canada East','Europe','Europe','Europe','Africa',
        'Europe','South','Europe','Europe','Canada West','Africa','South','South','Australia East','Australia West',
        'East','West','Europe','Europe','Europe','Europe','Europe','Europe','Europe','Europe',
        'Europe','Europe','Europe','Europe','Europe','Europe','Europe','Middle East','Asia','Asia',
        'Asia','Asia','Asia','Asia','Asia','North America','South America','South America','South America','South America'
    ],
    'product_name': [
        'Laptop','Mouse','Desk','Monitor','Chair','Pallet Racks','Conveyors','Packing Tables','Forklifts','Stretch Wrap',
        'Bins','Forklifts','Envelopes','Pallet Racks','Backpacks','Tables','Scanners','Printers','Pallets','Trolleys',
        'Shelving','Carts','Barrels','Crates','Hand Trucks','Forklift Batteries','Conveyor Belts','Shrink Wrap','Tape','Boxes',
        'Storage Bins','Packaging Tape','Pallet Wrap','Stretch Film','Label Printer','Scanner','Pallet Jacks','Roll Cages','Bins','Shelving Units',
        'Pallet Racks','Forklifts','Conveyors','Packing Tables','Stretch Wrap','Bins','Tables','Envelopes','Backpacks','Pallet Racks'
    ],
    'category': [
        'Electronics','Electronics','Furniture','Electronics','Furniture','Warehouse Equipment','Warehouse Equipment','Warehouse Equipment','Warehouse Equipment','Consumables',
        'Consumables','Warehouse Equipment','Consumables','Warehouse Equipment','Consumables','Furniture','Electronics','Electronics','Warehouse Equipment','Warehouse Equipment',
        'Warehouse Equipment','Warehouse Equipment','Warehouse Equipment','Warehouse Equipment','Warehouse Equipment','Warehouse Equipment','Warehouse Equipment','Consumables','Consumables','Consumables',
        'Consumables','Consumables','Consumables','Consumables','Electronics','Electronics','Warehouse Equipment','Warehouse Equipment','Consumables','Warehouse Equipment',
        'Warehouse Equipment','Warehouse Equipment','Warehouse Equipment','Warehouse Equipment','Consumables','Consumables','Furniture','Consumables','Consumables','Warehouse Equipment'
    ],
    'quantity': np.random.randint(1, 50, size=50),
    'unit_price': np.random.randint(5, 5000, size=50)
}

df = pd.DataFrame(data)

# -----------------
# CALCULATE TOTALS
# -----------------
df['total_price'] = df['quantity'] * df['unit_price']
df['profit'] = df['total_price'] * np.select(
    [
        df['category'] == 'Warehouse Equipment',
        df['category'] == 'Electronics',
        df['category'] == 'Furniture',
        df['category'] == 'Consumables'
    ],
    [0.30, 0.25, 0.25, 0.40],
    default=0.20
)

# New column for Tableau: total_sales = total_price + profit (or just total_price if preferred)
df['total_sales'] = df['total_price']  # You can use total_price or total_price + profit if desired

# -----------------
# SAVE CSV & EXCEL
# -----------------
df.to_csv('data/processed/sales_clean.csv', index=False)
df.to_excel('data/processed/sales_clean.xlsx', index=False)

print("sales_clean.csv and sales_clean.xlsx with total_sales created successfully!")