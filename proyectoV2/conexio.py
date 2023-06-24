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


# cmd.execute(
#     "UPDATE leyes SET Nombre_Ley = 'Ley de Teletrabajo' WHERE IDnumero_ley = 27555")
# conexion.commit()
# print("Registro modificado de manera exitosa")

# cmd.execute("DELETE FROM leyes WHERE IDnumero_ley = 20445")
# conexion.commit()
# print("Registro eliminado de manera exitosa")

# cmd.execute("select * from leyes")

# filas = cmd.fetchall()

# for x in filas:
#     print(x)
