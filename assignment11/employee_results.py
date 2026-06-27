import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Task 1: 

# Connect to the database
conn = sqlite3.connect("../db/lesson.db")

# SQL query
query = """
SELECT last_name, SUM(price * quantity) AS revenue
FROM employees e
JOIN orders o ON e.employee_id = o.employee_id
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY e.employee_id;
"""


employee_results = pd.read_sql_query(query, conn)


conn.close()

# Create bar chart
employee_results.plot(
    x="last_name",
    y="revenue",
    kind="bar",
    color="skyblue",
    title="Revenue by Employee",
    legend=False
)

plt.xlabel("Employee Last Name")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()