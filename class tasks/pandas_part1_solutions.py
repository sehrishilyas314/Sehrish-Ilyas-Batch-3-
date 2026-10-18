# Pandas Practice - Part 1 : All Solutions
import os
import numpy as np
import pandas as pd

sample_csv_text = """name,age,city,department,salary
Ali,28,Lahore,Engineering,85000
Sara,32,Karachi,Marketing,72000
Ahmed,45,Lahore,Engineering,120000
Ayesha,24,Islamabad,Sales,55000
Bilal,38,Karachi,Engineering,98000
Zainab,29,Islamabad,Marketing,68000
Usman,52,Lahore,Sales,60000
Hina,31,Karachi,Engineering,91000
"""

os.makedirs("sample_data", exist_ok=True)
with open("sample_data/employees.csv", "w") as file:
    file.write(sample_csv_text)


# ============================================================
# Pandas Part 1 - Task 1: Load and Inspect
# ============================================================
df = pd.read_csv("sample_data/employees.csv")

print("First 3 rows:")
print(df.head(3))
print("\nShape:", df.shape)
print("\nColumn data types:")
print(df.dtypes)


# ============================================================
# Pandas Part 1 - Task 2: Create a Series
# ============================================================
df = pd.read_csv("sample_data/employees.csv")

department_series = df["department"]

print("Unique values:", department_series.unique())
print("Number of unique values:", department_series.nunique())


# ============================================================
# Pandas Part 1 - Task 3: Select Columns
# ============================================================
df = pd.read_csv("sample_data/employees.csv")

name_salary = df[["name", "salary"]]
print(name_salary)


# ============================================================
# Pandas Part 1 - Task 4: Row Selection with .iloc[]
# ============================================================
df = pd.read_csv("sample_data/employees.csv")

# 4th row = position 3 (counting starts at 0)
print("4th row:")
print(df.iloc[3])

# Just the city of that row (city is column position 2)
print("\nCity of the 4th row:", df.iloc[3]["city"])


# ============================================================
# Pandas Part 1 - Task 5: Basic Filtering
# ============================================================
df = pd.read_csv("sample_data/employees.csv")

high_earners = df[df["salary"] > 80000]
print(high_earners)


# ============================================================
# Pandas Part 1 - Task 6: Combined Filtering
# ============================================================
df = pd.read_csv("sample_data/employees.csv")

# Each condition goes in its own brackets, joined with &
young_engineers = df[(df["department"] == "Engineering") & (df["age"] < 40)]
print(young_engineers)


# ============================================================
# Pandas Part 1 - Task 7: Add a Computed Column
# ============================================================
df = pd.read_csv("sample_data/employees.csv")

df["annual_bonus"] = df["salary"] * 0.10
print(df)


# ============================================================
# Pandas Part 1 - Task 8: .loc[] for Row + Column Selection
# ============================================================
df = pd.read_csv("sample_data/employees.csv")

# .loc[row_condition, [columns]]
karachi_staff = df.loc[df["city"] == "Karachi", ["name", "department"]]
print(karachi_staff)


# ============================================================
# Pandas Part 1 - Task 9: Handling Missing Data
# ============================================================
df = pd.read_csv("sample_data/employees.csv")

# Copy so the original df stays untouched
df_missing = df.copy()
df_missing.loc[[1, 4], "salary"] = np.nan

# (a) Missing values per column
print("Missing values per column:")
print(df_missing.isnull().sum())

# (b) Fill missing salary with the column average
avg_salary = df_missing["salary"].mean()
df_missing["salary"] = df_missing["salary"].fillna(avg_salary)

print("\nAfter filling with the average salary:")
print(df_missing)


# ============================================================
# Pandas Part 1 - Task 10: Sorting
# ============================================================
df = pd.read_csv("sample_data/employees.csv")

sorted_df = df.sort_values(by=["department", "salary"], ascending=[True, False])
print(sorted_df)


# ============================================================
# Pandas Part 1 - Task 11: Feature Engineering
# ============================================================
df = pd.read_csv("sample_data/employees.csv")

df["senior_employee"] = df["age"] >= 40

# Boolean indexing: only senior employees, selected columns
seniors = df.loc[df["senior_employee"], ["name", "age", "department"]]
print(seniors)


# ============================================================
# Pandas Part 1 - Task 12: Cleaning a Messier Dataset
# ============================================================
messy = {
    "name": ["Ali", "Sara", None, "Ayesha", "Bilal"],
    "age": [28, np.nan, 45, 24, 38],
    "salary": [85000, 72000, 120000, np.nan, 98000],
}
df = pd.DataFrame(messy)

# 1. Missing values per column
print("Missing values per column:")
print(df.isnull().sum())

# 2. Drop rows where name is missing
df = df.dropna(subset=["name"])

# 3. Fill remaining missing age/salary with that column's mean
df["age"] = df["age"].fillna(df["age"].mean())
df["salary"] = df["salary"].fillna(df["salary"].mean())

# 4. Final cleaned DataFrame
print("\nCleaned DataFrame:")
print(df)


# ============================================================
# Pandas Part 1 - Task 13: A Small Exploration Report
# ============================================================
df = pd.read_csv("sample_data/employees.csv")

total_employees = len(df)
average_salary = round(df["salary"].mean(), 2)

avg_by_dept = df.groupby("department")["salary"].mean()
top_department = avg_by_dept.idxmax()

top_earner = df.loc[df["salary"].idxmax(), "name"]

print("===== Employee Exploration Report =====")
print(f"Total employees           : {total_employees}")
print(f"Average salary            : {average_salary}")
print(f"Highest avg salary dept   : {top_department} ({avg_by_dept[top_department]:.2f})")
print(f"Highest-paid employee     : {top_earner}")
