"""
Generates a synthetic retail sales dataset for the Power BI Retail Sales Dashboard project.
Run: python generate_data.py
Output: retail_sales_data.csv
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

# --- Reference data ---
regions = {
    "East": ["New York", "Boston", "Philadelphia"],
    "West": ["Los Angeles", "San Francisco", "Seattle"],
    "Central": ["Chicago", "Dallas", "Minneapolis"],
    "South": ["Atlanta", "Miami", "Houston"],
}

categories = {
    "Furniture": ["Chairs", "Tables", "Bookcases", "Storage"],
    "Technology": ["Phones", "Accessories", "Laptops", "Printers"],
    "Office Supplies": ["Paper", "Binders", "Art", "Labels"],
}

segments = ["Consumer", "Corporate", "Home Office"]
ship_modes = ["Standard Class", "Second Class", "First Class", "Same Day"]

n_rows = 3000
start_date = datetime(2023, 1, 1)
end_date = datetime(2025, 12, 31)
date_range_days = (end_date - start_date).days

rows = []
for i in range(1, n_rows + 1):
    order_date = start_date + timedelta(days=int(np.random.randint(0, date_range_days)))
    ship_delay = np.random.randint(1, 7)
    ship_date = order_date + timedelta(days=ship_delay)

    region = np.random.choice(list(regions.keys()))
    city = np.random.choice(regions[region])

    category = np.random.choice(list(categories.keys()), p=[0.25, 0.35, 0.40])
    sub_category = np.random.choice(categories[category])

    segment = np.random.choice(segments, p=[0.5, 0.3, 0.2])
    ship_mode = np.random.choice(ship_modes, p=[0.6, 0.2, 0.15, 0.05])

    quantity = np.random.randint(1, 15)
    base_price = {
        "Furniture": np.random.uniform(50, 800),
        "Technology": np.random.uniform(30, 1500),
        "Office Supplies": np.random.uniform(2, 100),
    }[category]

    sales = round(base_price * quantity, 2)
    discount = np.random.choice([0, 0.1, 0.15, 0.2, 0.3], p=[0.4, 0.25, 0.15, 0.1, 0.1])
    discounted_sales = round(sales * (1 - discount), 2)

    margin_rate = {
        "Furniture": np.random.uniform(0.05, 0.25),
        "Technology": np.random.uniform(0.10, 0.35),
        "Office Supplies": np.random.uniform(0.15, 0.40),
    }[category]
    profit = round(discounted_sales * margin_rate - (discounted_sales * discount * 0.5), 2)

    customer_id = f"CUST-{np.random.randint(1000, 1200)}"

    rows.append({
        "Order_ID": f"ORD-{10000 + i}",
        "Order_Date": order_date.strftime("%Y-%m-%d"),
        "Ship_Date": ship_date.strftime("%Y-%m-%d"),
        "Ship_Mode": ship_mode,
        "Customer_ID": customer_id,
        "Segment": segment,
        "Region": region,
        "City": city,
        "Category": category,
        "Sub_Category": sub_category,
        "Quantity": quantity,
        "Sales": discounted_sales,
        "Discount": discount,
        "Profit": profit,
    })

df = pd.DataFrame(rows)
df = df.sort_values("Order_Date").reset_index(drop=True)
df.to_csv("retail_sales_data.csv", index=False)

print(f"Generated {len(df)} rows -> retail_sales_data.csv")
print(df.head())
