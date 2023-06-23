# Team_Rocket
Grupo de 10 personas ISPC

import mysql.connector

conexion1=mysql.connector.connect(host="localhost 3306", user="root", passwd="")
cursor1=conexion1.cursor()
cursor1.execute("show databases")
for base in cursor1:
    print(base)
conexion1.close()  