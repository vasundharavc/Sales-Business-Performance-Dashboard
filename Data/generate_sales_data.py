import pandas as pd
import numpy as np

np.random.seed(42)

# Number of sales transactions
n = 5000

# Product information
products = {
    "Laptop": ("Electronics", 65000, 52000),
    "Monitor": ("Electronics", 18000, 13500),
    "Keyboard": ("Accessories", 2200, 1400),
    "Mouse": ("Accessories", 1200, 700),
    "Headphones": ("Accessories", 3500, 2200),
    "Webcam": ("Accessories", 2800, 1700),
    "Smartphone": ("Electronics", 32000, 27000),
    "Tablet": ("Electronics", 24000, 19500),
    "Printer": ("Office Equipment", 12500, 9800),
    "Office Chair": ("Furniture", 9500, 7000),
    "Desk": ("Furniture", 12000, 9000),
    "External SSD": ("Storage", 8500, 6200)
}

locations = {
    "West": [
        ("Maharashtra", "Pune"),
        ("Maharashtra", "Mumbai"),
        ("Maharashtra", "Nashik"),
        ("Gujarat", "Ahmedabad"),
        ("Gujarat", "Surat"),
        ("Goa", "Panaji")
    ],
    "North": [
        ("Delhi", "New Delhi"),
        ("Haryana", "Gurugram"),
        ("Punjab", "Ludhiana"),
        ("Uttar Pradesh", "Noida"),
        ("Rajasthan", "Jaipur")
    ],
    "South": [
        ("Karnataka", "Bengaluru"),
        ("Telangana", "Hyderabad"),
        ("Tamil Nadu", "Chennai"),
        ("Kerala", "Kochi"),
        ("Andhra Pradesh", "Vijayawada")
    ],
    "East": [
        ("West Bengal", "Kolkata"),
        ("Odisha", "Bhubaneswar"),
        ("Bihar", "Patna"),
        ("Jharkhand", "Ranchi"),
        ("Assam", "Guwahati")
    ]
}

first_names = [
    "Aarav", "Aditya", "Ananya", "Arjun", "Diya",
    "Ishaan", "Kavya", "Meera", "Neha", "Rahul",
    "Riya", "Rohan", "Sneha", "Tanvi", "Vikram",
    "Priya", "Karan", "Nisha", "Pooja", "Sahil"
]

last_names = [
    "Sharma", "Patil", "Verma", "Gupta", "Joshi",
    "Chaudhary", "Deshmukh", "Kulkarni", "Singh",
    "Mehta", "Shah", "Yadav", "Nair", "Reddy", "Iyer"
]

payment_modes = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Cash on Delivery"
]

product_names = list(products.keys())
region_names = list(locations.keys())

# Generate dates for 2025
dates = pd.date_range(
    start="2025-01-01",
    end="2025-12-31"
)

rows = []

for i in range(n):

    product = np.random.choice(product_names)

    category, unit_price, unit_cost = products[product]

    region = np.random.choice(
        region_names,
        p=[0.35, 0.25, 0.25, 0.15]
    )

    state, city = locations[region][
        np.random.randint(len(locations[region]))
    ]

    quantity = np.random.choice(
        [1, 2, 3, 4, 5],
        p=[0.48, 0.28, 0.14, 0.07, 0.03]
    )

    price_variation = np.random.choice(
        [0.95, 1.00, 1.05],
        p=[0.10, 0.80, 0.10]
    )

    selling_price = round(
        unit_price * price_variation,
        2
    )

    sales = round(
        selling_price * quantity,
        2
    )

    cost = round(
        unit_cost * quantity,
        2
    )

    profit = round(
        sales - cost,
        2
    )

    first_name = np.random.choice(first_names)
    last_name = np.random.choice(last_names)

    customer_name = f"{first_name} {last_name}"

    customer_id = f"CUST{np.random.randint(1001, 2001)}"

    rows.append([
        f"ORD{100001 + i}",
        np.random.choice(dates),
        customer_id,
        customer_name,
        product,
        category,
        quantity,
        selling_price,
        sales,
        cost,
        profit,
        region,
        state,
        city,
        np.random.choice(payment_modes)
    ])

# Create DataFrame
df = pd.DataFrame(
    rows,
    columns=[
        "Order_ID",
        "Order_Date",
        "Customer_ID",
        "Customer_Name",
        "Product",
        "Category",
        "Quantity",
        "Unit_Price",
        "Sales",
        "Cost",
        "Profit",
        "Region",
        "State",
        "City",
        "Payment_Mode"
    ]
)

# Save CSV
df.to_csv(
    "sales_data.csv",
    index=False
)

print("===================================")
print("Sales dataset created successfully!")
print("===================================")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print("File: sales_data.csv")
print("===================================")
print("\nFirst 5 records:")
print(df.head())