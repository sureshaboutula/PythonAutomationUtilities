import mysql.connector
from utilities.configurations import *

# connect() - To connect to Database
# cursor() - To execute queries
# fetchone - Returns first row of the table
# fetchall - Retuens all rows
#host=localhost, database=PythonAutomation, username, password
# conn = mysql.connector.connect(
#     host='localhost',
#     database='PythonAutomation',
#     user='root',
#     password='Sureshsql@2789'
# )
conn = getdbConnection()

print(conn.is_connected())

cursor = conn.cursor()
cursor.execute('select * from CustomerInfo')
# row = cursor.fetchone()
# print(row) # Result is Tuple
# print(row[3])
# rows = cursor.fetchall() # It does not return the first row as it was already fetched by fetchone method
# print(rows) # Result is List of Tuples
# print(rows[0])
rows = cursor.fetchall()
print(type(rows))
print(rows)
sum = 0
for row in rows:
    sum = sum + row[2]

print(sum)
assert sum == 340

# query = "update CustomerInfo set Location = %s where CourseName = %s"
# data = ("UK", "Jmeter")
# cursor.execute(query, data)
# conn.commit()

query = "delete from CustomerInfo where CourseName = %s"
data = ("WebServices",)
cursor.execute(query, data)
conn.commit()

conn.close()