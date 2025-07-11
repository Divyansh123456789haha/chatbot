import sqlite3

# Connect to SQLite DB (creates it if it doesn't exist)
conn = sqlite3.connect("darkcoal.db")
cursor = conn.cursor()

# Drop tables if they exist (for restarting development/testing)
cursor.execute("DROP TABLE IF EXISTS product_variants")
cursor.execute("DROP TABLE IF EXISTS products")

# Create the main products table
cursor.execute("""
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT CHECK(category IN ('Street Style', 'Classy Polo')),
    description TEXT,
    price INTEGER,
    image_url TEXT
)
""")

# Create the product_variants table for sizes, fits, availability
cursor.execute("""
CREATE TABLE product_variants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    size TEXT CHECK(size IN ('S', 'M', 'L', 'XL', 'XXL')),
    fit TEXT CHECK(fit IN ('Regular', 'Street')),
    available BOOLEAN,
    discount INTEGER DEFAULT 0,
    FOREIGN KEY(product_id) REFERENCES products(id)
)
""")

# Sample product insert
cursor.execute("""
INSERT INTO products (name, category, description, price, image_url)
VALUES (?, ?, ?, ?, ?)
""", ("Midnight Black Hoodie", "Street Style", "Premium street hoodie", 1299, "images/hoodie1.jpg"))

product_id = cursor.lastrowid

# Insert size variants for this product
sizes = ['S', 'M', 'L', 'XL', 'XXL']
for size in sizes:
    cursor.execute("""
    INSERT INTO product_variants (product_id, size, fit, available, discount)
    VALUES (?, ?, ?, ?, ?)
    """, (product_id, size, "Street", True, 10))  # all sizes available with 10% discount

# Commit changes and close
conn.commit()
conn.close()

print("✅ Database and tables created successfully.")

