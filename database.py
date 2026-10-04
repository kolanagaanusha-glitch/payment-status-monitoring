import sqlite3

connection = sqlite3.connect("payment.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS payments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    transaction_id TEXT UNIQUE,
    customer_name TEXT,
    amount REAL,
    status TEXT
)
""")

cursor.execute("""
INSERT OR IGNORE INTO payments
(transaction_id, customer_name, amount, status)
VALUES
('TXN101', 'Anusha', 500, 'SUCCESS')
""")

cursor.execute("""
INSERT OR IGNORE INTO payments
(transaction_id, customer_name, amount, status)
VALUES
('TXN102', 'Ravi', 1000, 'PENDING')
""")

cursor.execute("""
INSERT OR IGNORE INTO payments
(transaction_id, customer_name, amount, status)
VALUES
('TXN103', 'Priya', 750, 'FAILED')
""")

connection.commit()

connection.close()

print("Payment data added successfully!")