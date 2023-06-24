import mysql.connector

# Clase Ley
class Ley:
    def __init__(self, numero, descripcion):
        self.numero = numero
        self.descripcion = descripcion

# Clase para interactuar con la base de datos
class GestorBD:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="tu_usuario",
            password="tu_contraseña",
            database="nombre_base_de_datos"
        )
        self.cursor = self.conexion.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS leyes (
                                numero VARCHAR(100),
                                descripcion VARCHAR(255)
                            )''')
        self.conexion.commit()

    def insertar_ley(self, ley):
        query = "INSERT INTO leyes (numero, descripcion) VALUES (%s, %s)"
        valores = (ley.numero, ley.descripcion)
        self.cursor.execute(query, valores)
        self.conexion.commit()

    def buscar_ley_por_numero(self, numero):
        query = "SELECT * FROM leyes WHERE numero = %s"
        valores = (numero,)
        self.cursor.execute(query, valores)
        return self.cursor.fetchone()

    def buscar_ley_por_palabra_clave(self, palabra_clave):
        query = "SELECT * FROM leyes WHERE descripcion LIKE %s"
        valores = ('%' + palabra_clave + '%',)
        self.cursor.execute(query, valores)
        return self.cursor.fetchall()

    def actualizar_ley(self, ley):
        query = "UPDATE leyes SET descripcion = %s WHERE numero = %s"
        valores = (ley.descripcion, ley.numero)
        self.cursor.execute(query, valores)
        self.conexion.commit()

    def eliminar_ley(self, numero):
        query = "DELETE FROM leyes WHERE numero = %s"
        valores = (numero,)
        self.cursor.execute(query, valores)
        self.conexion.commit()

    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()

# Función para mostrar las opciones disponibles
def mostrar_menu():
    print("1. Consultar ley por número")
    print("2. Consultar ley por palabra clave")
    print("3. Insertar nueva ley")
    print("4. Actualizar ley")
    print("5. Eliminar ley")
    print("6. Salir")

# Función principal del programa
def main():
    gestor_bd = GestorBD()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero = input("Ingrese el número de la ley: ")
            ley = gestor_bd.buscar_ley_por_numero(numero)
            if ley:
                print("Número de Ley:", ley[0])
                print("Descripción:", ley[1])
            else:
                print("La ley no fue encontrada.")

        elif opcion == "2":
            palabra_clave = input("Ingrese una palabra clave: ")
            leyes = gestor_bd.buscar_ley_por_palabra_clave(palabra_clave)
            if leyes:
                for ley in leyes:
                    print("Número de Ley:", ley[0])
                    print("Descripción:", ley[1])
            else:
                print("No se encontraron leyes con esa palabra clave.")

        elif opcion == "3":
            numero = input("Ingrese el número de la ley: ")
            descripcion = input("Ingrese la descripción de la ley: ")
            nueva_ley = Ley(numero, descripcion)
            gestor_bd.insertar_ley(nueva_ley)
            print("La ley se ha insertado correctamente.")

        elif opcion == "4":
            numero = input("Ingrese el número de la ley a actualizar: ")
            descripcion = input("Ingrese la nueva descripción de la ley: ")
            nueva_ley = Ley(numero, descripcion)
            gestor_bd.actualizar_ley(nueva_ley)
            print("La ley se ha actualizado correctamente.")

        elif opcion == "5":
            numero = input("Ingrese el número de la ley a eliminar: ")
            gestor_bd.eliminar_ley(numero)
            print("La ley se ha eliminado correctamente.")

        elif opcion == "6":
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

    gestor_bd.cerrar_conexion()

if __name__ == '__main__':
    main()
