import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    database = "proyecto_integral_",
    user = "root",
    password = ""
) #CONECTOR DE MYSQL A PYTHON

def search_Leyes_Names(por_Nombres):
    sql = "SELECT nombre_normativa FROM `proyecto_integral_`.`ley`; = " + str(por_Nombres)
    cursor = conn.cursor() 
    cursor.execute(sql)
    serie = cursor.fetchall()
    print(serie)

def search_Leyes_Number(por_Number):
    sql = "SELECT numero_normativa * FROM `proyecto_integral_`.`ley` = " + str(por_Number)
    cursor = conn.cursor() 
    cursor.execute(sql)
    serie = cursor.fetchall()
    print(serie)

