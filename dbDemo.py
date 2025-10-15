import mysql.connector
from utilities.configurations import *

# mydb = mysql.connector.connect(host="localhost",database= 'APIDevelop', user="root", password="root")

mydb = getConnection()
print(mydb.is_connected())

cursor = mydb.cursor()

cursor.execute('select * from CustomerInfo')
# # row = cursor.fetchone()
# # print(row)
# # print(row[3])
# rowALL = cursor.fetchall()
# print(rowALL)
# print(rowALL[2])

rows = cursor.fetchall()
print(type(rows))
print(rows)
sum = 0
for row in rows:
    sum = sum + row[2]
print(sum)
assert sum == 340

query = "Update CustomerInfo set Location = %s where CourseName = %s"
data = ("India", "Jmeter")
cursor.execute(query, data)
mydb.commit()








mydb.close()