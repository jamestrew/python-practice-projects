import sqlite3
from employee import Employee

conn = sqlite3.connect('employee.db')  # use ':memory:' for an in-memory db

c = conn.cursor()

# c.execute("""CREATE TABLE employees (
#                 first TEXT,
#                 last TEXT,
#                 pay INTEGER
#         )
#     """)

# c.execute("INSERT INTO employees (first, last, pay) VALUES ('Corey', 'Schafer', 50000)")
# c.execute("INSERT INTO employees (first, last, pay) VALUES ('Mary', 'Schafer', 50000)")


emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)

# two ways to pass args (don't use traditional python methods)
# c.execute("INSERT INTO employees (first, last, pay) VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))
# c.execute("INSERT INTO employees (first, last, pay) VALUES (:first, :last, :pay)",
#           {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})


c.execute("SELECT * FROM employees")  # returns iterator

# use fetch to iterate through the query results
# fetchone() gets first one
# fetchmany(50) gets the 50
# fetchall() gets all

print(c.fetchall())


conn.commit()
conn.close()
