
import mariadb 
import sys
conn = mariadb.connect(
    user = 'root',
    password = 'Vikrants298@',
    host = 'localhost',
    port = 3306,
    database= 'employees'
 )
cur = conn.cursor()
conn.autocommit = True
try:
    cur.execute('CREATE TABLE customer (name VARCHAR(30),age INTEGER)')
except Exception as y:
    print(y)
cur.execute('INSERT INTO customer (name,age) VALUES("Anusha",22),("Monica",22),("test",23)')
cur.execute('SELECT name,age FROM customer')
''''for (name1,age) in cur:
print('Name:',(name1),'Age',(age))'''

