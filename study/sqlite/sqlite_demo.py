import sqlite3

conn = sqlite3.connect('employee.db')  # use ':memory:' for an in-memory db

c = conn.cursor()

c.execute("""CREATE TABLE employees (
                first TEXT,
                last TEXT,
                pay INTEGER
        )
    """)
