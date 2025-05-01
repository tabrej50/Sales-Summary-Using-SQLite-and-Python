# Sales Summary Using SQLite and Python

## Objective
Get a basic sales summary from a SQLite database using SQL inside Python.

## Tools Used
- Python
- sqlite3
- pandas
- matplotlib

## Steps Performed
1. Created `sales_data.db` with 100 sample sales records.
2. Queried total quantity and total revenue per product.
3. Displayed results using print and a bar chart.

## SQL Query Used
```sql
SELECT 
    product, 
    SUM(quantity) AS total_quantity, 
    SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY product
