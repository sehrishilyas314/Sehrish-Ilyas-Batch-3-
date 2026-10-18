# Pandas Practice - Part 2 : All Solutions
import os
import numpy as np
import pandas as pd

orders_csv_text = """order_id,customer,city,product,category,quantity,unit_price,order_date
1,Ali,Lahore,Laptop,Electronics,1,1200,2024-01-05
2,Sara,Karachi,Mouse,Electronics,3,25,2024-01-06
3,Ahmed,Lahore,Desk,Furniture,1,300,2024-01-15
4,Ayesha,Islamabad,Chair,Furniture,4,150,2024-01-20
5,Ali,Lahore,Monitor,Electronics,2,220,2024-02-02
6,Bilal,Karachi,Laptop,Electronics,1,1200,2024-02-10
7,Sara,Karachi,Desk,Furniture,2,300,2024-02-14
8,Zainab,Islamabad,Chair,Furniture,3,150,2024-02-25
9,Ahmed,Lahore,Monitor,Electronics,1,220,2024-03-01
10,Ayesha,Islamabad,Mouse,Electronics,5,25,2024-03-04
11,Ali,Lahore,Chair,Furniture,2,150,2024-03-08
12,Bilal,Karachi,Monitor,Electronics,2,220,2024-03-18
"""

os.makedirs("sample_data", exist_ok=True)
with open("sample_data/orders.csv", "w") as file:
    file.write(orders_csv_text)


# ============================================================
# Pandas Part 2 - Task 1: Load and Add a Revenue Column
# ============================================================
orders = pd.read_csv("sample_data/orders.csv")
orders["order_date"] = pd.to_datetime(orders["order_date"])
orders["revenue"] = orders["quantity"] * orders["unit_price"]

print(orders)
print("\nData types:")
print(orders.dtypes)


# ============================================================
# Pandas Part 2 - Task 2: Group and Aggregate
# ============================================================
orders = pd.read_csv("sample_data/orders.csv")
orders["order_date"] = pd.to_datetime(orders["order_date"])
orders["revenue"] = orders["quantity"] * orders["unit_price"]

revenue_by_category = orders.groupby("category")["revenue"].sum()
print(revenue_by_category)


# ============================================================
# Pandas Part 2 - Task 3: Multiple Aggregations
# ============================================================
orders = pd.read_csv("sample_data/orders.csv")
orders["order_date"] = pd.to_datetime(orders["order_date"])
orders["revenue"] = orders["quantity"] * orders["unit_price"]

city_stats = orders.groupby("city")["revenue"].agg(["sum", "mean"])
print(city_stats)


# ============================================================
# Pandas Part 2 - Task 4: String Cleaning
# ============================================================
orders = pd.read_csv("sample_data/orders.csv")

orders["product_upper"] = orders["product"].str.upper()
print(orders[["product", "product_upper"]])


# ============================================================
# Pandas Part 2 - Task 5: Duplicate Check
# ============================================================
orders = pd.read_csv("sample_data/orders.csv")

# Part 1: exact duplicates in orders
print("Duplicate rows in orders:", orders.duplicated().sum())

# Part 2: small DataFrame with an intentional duplicate
small = pd.DataFrame({
    "name": ["Ali", "Sara", "Ali", "Bilal"],
    "city": ["Lahore", "Karachi", "Lahore", "Karachi"],
})
print("\nBefore drop_duplicates:")
print(small)

small_clean = small.drop_duplicates()
print("\nAfter drop_duplicates:")
print(small_clean)


# ============================================================
# Pandas Part 2 - Task 6: Named Aggregation
# ============================================================
orders = pd.read_csv("sample_data/orders.csv")
orders["revenue"] = orders["quantity"] * orders["unit_price"]

summary = orders.groupby("city").agg(
    total_orders=("order_id", "count"),
    total_revenue=("revenue", "sum"),
)
print(summary)


# ============================================================
# Pandas Part 2 - Task 7: Merge with Extra Data
# ============================================================
orders = pd.read_csv("sample_data/orders.csv")

city_region = pd.DataFrame({
    "city": ["Lahore", "Karachi", "Islamabad"],
    "region": ["Punjab", "Sindh", "Federal"],
})

# how="left": orders is the main table, so we keep EVERY order even if a
# city is missing from city_region (its region would just be NaN).
# An "inner" merge could silently drop such orders.
merged = orders.merge(city_region, on="city", how="left")

print(merged[["order_id", "customer", "city", "region"]])


# ============================================================
# Pandas Part 2 - Task 8: Pivot Table
# ============================================================
orders = pd.read_csv("sample_data/orders.csv")
orders["order_date"] = pd.to_datetime(orders["order_date"])
orders["revenue"] = orders["quantity"] * orders["unit_price"]

pivot = pd.pivot_table(
    orders,
    values="revenue",
    index="category",
    columns="city",
    aggfunc="sum",
    fill_value=0,
)
print(pivot)


# ============================================================
# Pandas Part 2 - Task 9: Apply with a Custom Function
# ============================================================
orders = pd.read_csv("sample_data/orders.csv")
orders["order_date"] = pd.to_datetime(orders["order_date"])
orders["revenue"] = orders["quantity"] * orders["unit_price"]

def label_order(quantity):
    if quantity >= 3:
        return "Bulk"
    return "Regular"


orders["order_type"] = orders["quantity"].apply(label_order)
print(orders[["order_id", "quantity", "order_type"]])


# ============================================================
# Pandas Part 2 - Task 10: Dates
# ============================================================
orders = pd.read_csv("sample_data/orders.csv")
orders["order_date"] = pd.to_datetime(orders["order_date"])
orders["revenue"] = orders["quantity"] * orders["unit_price"]

orders["order_month"] = orders["order_date"].dt.to_period("M")
orders["order_weekday"] = orders["order_date"].dt.day_name()

print(orders[["order_id", "order_date", "order_month", "order_weekday"]])

weekday_revenue = orders.groupby("order_weekday")["revenue"].sum()
print("\nRevenue per weekday:")
print(weekday_revenue)
print("\nWeekday with highest total revenue:", weekday_revenue.idxmax())


# ============================================================
# Pandas Part 2 - Task 11: Customer-Level Feature Engineering
# ============================================================
orders = pd.read_csv("sample_data/orders.csv")
orders["order_date"] = pd.to_datetime(orders["order_date"])
orders["revenue"] = orders["quantity"] * orders["unit_price"]

# total_orders, total_spent, average_order_value
customer_summary = orders.groupby("customer").agg(
    total_orders=("order_id", "count"),
    total_spent=("revenue", "sum"),
    average_order_value=("revenue", "mean"),
)

# favorite_category: count orders per (customer, category), keep the top one.
# Ties are broken alphabetically by category so the result is deterministic.
category_counts = (
    orders.groupby(["customer", "category"])
    .size()
    .reset_index(name="order_count")
)
category_counts = category_counts.sort_values(
    by=["customer", "order_count", "category"],
    ascending=[True, False, True],
)
favorite = (
    category_counts.drop_duplicates(subset="customer")
    .set_index("customer")["category"]
    .rename("favorite_category")
)

customer_summary = customer_summary.join(favorite).reset_index()
print(customer_summary)


# ============================================================
# Pandas Part 2 - Task 12: Monthly Trend and Growth
# ============================================================
orders = pd.read_csv("sample_data/orders.csv")
orders["order_date"] = pd.to_datetime(orders["order_date"])
orders["revenue"] = orders["quantity"] * orders["unit_price"]

orders["order_month"] = orders["order_date"].dt.to_period("M")

monthly_revenue = orders.groupby("order_month")["revenue"].sum()
print("Monthly revenue:")
print(monthly_revenue)

# Series.diff() = this month minus previous month (first month is NaN)
mom_change = monthly_revenue.diff()
print("\nMonth-over-month change:")
print(mom_change)


# ============================================================
# Pandas Part 2 - Task 13: End-to-End Mini Report
# ============================================================
orders = pd.read_csv("sample_data/orders.csv")
orders["order_date"] = pd.to_datetime(orders["order_date"])
orders["revenue"] = orders["quantity"] * orders["unit_price"]

# total_revenue, total_orders, average_order_value per city
city_summary = orders.groupby("city").agg(
    total_revenue=("revenue", "sum"),
    total_orders=("order_id", "count"),
    average_order_value=("revenue", "mean"),
)

# top_category: category with the most revenue in each city
cat_revenue = (
    orders.groupby(["city", "category"])["revenue"]
    .sum()
    .reset_index()
    .sort_values(by=["city", "revenue"], ascending=[True, False])
)
top_category = (
    cat_revenue.drop_duplicates(subset="city")
    .set_index("city")["category"]
    .rename("top_category")
)

city_summary = city_summary.join(top_category).reset_index()
print("Final summary:")
print(city_summary)

# Export to CSV and JSON
city_summary.to_csv("sample_data/city_summary.csv", index=False)
city_summary.to_json("sample_data/city_summary.json", orient="records", indent=2)

# Reload and confirm round-trip
print("\nReloaded from CSV:")
print(pd.read_csv("sample_data/city_summary.csv"))

print("\nReloaded from JSON:")
print(pd.read_json("sample_data/city_summary.json", orient="records"))
