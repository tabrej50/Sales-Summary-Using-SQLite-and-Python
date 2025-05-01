#!/usr/bin/env python
# coding: utf-8

# In[5]:


import sqlite3
import random

conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

products = ['Apple', 'Banana', 'Orange', 'Grapes', 'Mango', 'Peach', 'Pineapple', 'Strawberry', 'Watermelon', 'Blueberry']

sample_data = []
for _ in range(100):
    product = random.choice(products)
    quantity = random.randint(1, 20)
    price = round(random.uniform(1.0, 5.0), 2)
    sample_data.append((product, quantity, price))

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)

conn.commit()
conn.close()

print("Inserted 100 records into sales_data.db")


# In[6]:


import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("sales_data.db")

query = """
SELECT 
    product, 
    SUM(quantity) AS total_quantity, 
    SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY product
"""

df = pd.read_sql_query(query, conn)

print("Sales Summary:")
print(df)

plt.figure(figsize=(10, 6))
df.plot(kind='bar', x='product', y='total_revenue', color='skyblue', legend=False)
plt.title("Total Revenue by Product")
plt.ylabel("Revenue")
plt.xlabel("Product")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()

conn.close()


# In[ ]:




