# pip install mysql-connector-python

import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="proyecto_integral_",
    user="root",
    password="")  # rocio1820 poner contrasenia su corresponde


def buscar_ley_por_numero(numero_ley):
    sql = "select * from ley where numero_normativa = " + str(numero_ley)
    cmd = conexion.cursor()  # crear cursor
    cmd.execute(sql)
    filas = cmd.fetchall()
    print(filas)


def buscar_ley_por_palabras(numero_ley):
    sql = "select * from ley where nombre_normativa like '%" + \
        str(numero_ley) + "%'"
    cmd = conexion.cursor()  # crear cursor
    cmd.execute(sql)
    filas = cmd.fetchall()
    print(filas)

