import mysql.connector
from utilities.configurations import *

#host, database, user, password
#conn = mysql.connector.connect(host='localhost', database='APIDevelop', user='root', password='365Pass')
connonection1= getConnection()
connonection1.is_connected()
print(connonection1.is_connected())


print("***************************  1")
cursor23 = connonection1.cursor()
cursor23.execute('select * from Books')
row=cursor23.fetchone()
table_books=cursor23.fetchall()
print("*************************** 2")
print(row)
print(row[0])
print(type(row))
print(table_books)
print(type(table_books))
print(table_books[0][0])
print("***************************  3")
sum = 0
for book in table_books:
    sum = sum + int(book[2])
print(sum)
assert sum==257
print("***************************  4")
conn2=mysql.connector.connect(host='localhost', database='employees', user='root', password='365Pass')
conn2.is_connected()
print("***************************  5")
print(conn2.is_connected())
#SELECT * FROM employees.employees
print("***************************  6")
cursor2=conn2.cursor()
cursor2.execute('SELECT * FROM employees.employees')
row_employee=cursor2.fetchone()
print(row_employee)

print("***************************  7")

"""
query="update customerInfo set Location = %s where CourseName = %s"
data=("UK","Jmeter")
cursor2.execute(query,data)

print("***************************  8")
connonection1.commit()
#delete from customerInfo where courseName = 'WebServices';
query_delete="delete from customerInfo where courseName = 'WebServices';"

cursor2.execute(query_delete)
connonection1.commit()
"""

