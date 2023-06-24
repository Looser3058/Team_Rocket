import conexio  # traer clase de conexion a bd


class Ley:

    def __init__(self, numero_ley, nombre_ley):
        self.numero_ley = numero_ley
        self.nombre_ley = nombre_ley


class Operaciones:
    def __init__(self) -> None:
        pass

    def buscar_por_numero(self, numero_ley):
        print(numero_ley)
        conexio.buscar_ley_por_numero(numero_ley=numero_ley)

    def buscar_por_palabras_clave(self, palabras_clave):
        print(palabras_clave)
        conexio.buscar_ley_por_palabras(palabras_clave)

    def ingresar_nueva_ley(self, nueva_ley):
        print("insertar")

    def actualizar_ley(self, numero_ley):
        print("actualizar")

    def eliminar_ley(self, numero_ley):
        print("eliminar")

# Ley1 = Ley ("27555", "Ley de Teletrabajo", "trabajo, empleador, empleado, ley de contrato de trabajo, ministerio de trabajo empleo y seguridad de la nacion")
# Ley2 = Ley ("20744", "Ley de Contrato de trabajo", "ley de contrato de trabajo, relación laboral, empleador, empleado, legislación labora")
# Ley3 = Ley ("7642", "Ley de Ejercicio Profesional", "ley de ejercicio profesional, ciencias informáticas, ejercicio profesional, profesionales, matrícula")


# Ley1.buscar_por_numero ()
# Ley1.buscar_por_palabras_clave ()
op = Operaciones()  # se crea objeto ley
opcion = "0"  # deja opcion distinto de la opcion para terminar while

while opcion != "salir":  # programa correra hasta que se coloque salir en opciones
    print("Seleccione una opcion: \n")
    print("Opcion 1: buscar ley por numero : \n")
    print("Opcion 2: buscar ley por palabras : \n")
    print("Opcion 3: ingresar nueva ley : \n")
    print("Opcion 4: actualizar ley : \n")
    print("Opcion 5: eliminar una ley : \n")
    print("Opcion 6: Salir del programa : \n")
    opcionNumero = input("opcion : \n")
    if opcionNumero == "1":
        # try:
        numero = int(input("Ingrese el numero de ley: \n"))
        print("numero ingresado", numero)
        op.buscar_por_numero(numero)
        # except:
        #     print("Lo que ingreso no es un numero. \n")
    elif opcionNumero == "2":
        palabras = input("Ingrese las palabras a buscar")
        op.buscar_por_palabras_clave(palabras)
    elif opcionNumero == "3":
        numeroLeyNueva = int(input("Ingrese el numero de Ley"))
        nombreLeyNueva = input("Ingrese el descripcion de la ley")
        nuevaLey = Ley(numeroLeyNueva, nombreLeyNueva)
        op.ingresar_nueva_ley(nuevaLey)
    elif opcionNumero == "4":
        op.actualizar_ley()
    elif opcionNumero == "5":
        try:
            numero = int(input("Ingrese el numero de ley: \n"))
            op.eliminar_ley(numero)
        except:
            print("Lo que ingreso no es un numero. \n")

    elif opcionNumero == "6":
        opcion = "salir"
