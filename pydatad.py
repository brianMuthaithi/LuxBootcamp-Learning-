#connecting python with mysql
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'lux_test'
)
print(mydb)
cursor  = mydb.cursor()
# cursor.execute("CREATE TABLE waras(name VARCHAR(255), code_number VARCHAR(255))")
cursor.execute("SHOW TABLES")
for x in cursor:
    print(x)


