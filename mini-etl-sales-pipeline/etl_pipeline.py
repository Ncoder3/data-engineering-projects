
import pandas as pd

# Step 1: Extract
df = pd.read_csv("raw_sales.csv")

# Step 2: Transform
# Rename columns
df.columns = [col.strip().lower().replace(" ", "_").replace("($)", "usd") for col in df.columns]

# Fill missing customer names
df["customer_name"].fillna("Unknown", inplace=True)

# Remove rows with missing or invalid amount
df = df[df["amount_usd"].notnull()]
df = df[df["amount_usd"] != "NaN"]

# Convert order_date to datetime
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

# Step 3: Load
df.to_csv("cleaned_sales.csv", index=False)

print("ETL pipeline completed. Cleaned data saved to cleaned_sales.csv.")
