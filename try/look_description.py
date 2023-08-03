import sqlite3
connection = sqlite3.connect('sqlite.db')
cursor = connection.execute('select * from Student')
names = [description[0] for description in cursor.description]
connection.close()
print(names)

cursor = connection.execute('select * from Student')
# instead of cursor.description:
row = cursor.fetchone()
names = row.keys()
connection.close()
print(names)

connection.row_factory = sqlite3.Row
cursor = connection.execute('PRAGMA table_info(Student)')
desc = cursor.fetchall()
# getting names using list comprehension
names = [fields[1] for fields in desc]
connection.close()
print(names)