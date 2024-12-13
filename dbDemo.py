import mysql.connector
from utilities.configurations import *

#host, database, user, password
#conn = mysql.connector.connect(host='localhost', database='APIDevelop', user='root', password='365Pass')
connonection1= getConnection()
connonection1.is_connected()
print(connonection1.is_connected())

cursor = connonection1.cursor()
cursor.execute('select * from Books')
row=cursor.fetchone()
table_books=cursor.fetchall()
print(row)
print(row[0])
print(type(row))
print(table_books)
print(type(table_books))
print(table_books[0][0])

sum = 0
for book in table_books:
    sum = sum + int(book[2])
print(sum)
assert sum==257

conn2=mysql.connector.connect(host='localhost', database='employees', user='root', password='365Pass')
conn2.is_connected()
print("***************************")
print(conn2.is_connected())
#SELECT * FROM employees.employees
print("***************************")
cursor2=conn2.cursor()
cursor2.execute('SELECT * FROM employees.employees')
row_employee=cursor2.fetchone()
print(row_employee)


query="update customerInfo set Location = %s where CourseName = %s"
data=("USA","Jmeter")
cursor.execute(query,data)

conn.commit()
#delete from customerInfo where courseName = 'WebServices';
query_delete="delete from customerInfo where courseName = 'WebServices';"

cursor.execute(query_delete)
conn.commit()