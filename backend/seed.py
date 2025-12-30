import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "app.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# ---- CREATE TABLES ----
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    amount REAL,
    created_at TEXT,
    FOREIGN KEY(customer_id) REFERENCES customers(id)
)
""")

# ---- CLEAR OLD DATA ----
cursor.execute("DELETE FROM customers")
cursor.execute("DELETE FROM orders")

# ---- INSERT CUSTOMERS ----
customers = [
    (1, "Alice", "alice@gmail.com"),
    (2, "Bob", "bob@gmail.com"),
    (3, "Charlie", "charlie@gmail.com")
]

cursor.executemany(
    "INSERT INTO customers (id, name, email) VALUES (?, ?, ?)",
    customers
)

# ---- INSERT ORDERS ----
orders = [
    (1, 1, 120.50, "2024-01-01"),
    (2, 1, 80.00, "2024-01-05"),
    (3, 2, 200.00, "2024-01-03"),
    (4, 3, 50.00, "2024-01-07"),
    (5, 2, 75.25, "2024-01-09")
]

cursor.executemany(
    "INSERT INTO orders (id, customer_id, amount, created_at) VALUES (?, ?, ?, ?)",
    orders
)

conn.commit()
conn.close()

print("✅ Database seeded successfully!")
