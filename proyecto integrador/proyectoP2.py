import proyecto

class Leyes:
    def __init__(self, por_Nombres, por_Number):
        self.por_Nombres = por_Nombres
        self.por_Number = por_Number

class Busqueda:
    def __init__(self) -> None:
        pass
        
    def search_nombres(self, por_Nombres):
        print(por_Nombres)
        proyecto.search_Leyes_Names(por_Nombres=por_Nombres)
    
    def search_numbers(self, por_Number):
        print(por_Number)
        proyecto.search_Leyes_Number(por_Number=por_Number)
    
    def delete_ley(self, por_Nombres):
        print("Eliminar")
    
    def update_ley(self, por_Nombres):
        print("Actualización")
    
    def new_ley(self, por_Nombres):
        print("Agregar")
            
Ob = Busqueda()#funciona para la busquedas del if 

print("Entrando a la aplicacion")
print("Bienvenido!!, Elija que ley desea ver\n")
print("*RECOMENDACIÓN: PUEDE BUSCAR LA LEY POR SU NOMBRE O POR SU NUMERO\n")
print("1) Buscar la ley por numero\n")
print("2) Buscar la ley por el nombre\n")
print("OTRA OPCIONES:\n")
print("3) Agregar LEY\n")
print("4) Eliminar LEY\n")
print("5) Actualizar LEY\n")

Opcion = input("Ingrese la opción que desea: \n")
if Opcion == "1":
    numero = int(input("PON EL NUMERO DE LA LEY: \n"))
    print("Buscando...")
    Ob.search_numbers(numero)
elif Opcion == "2":
    Nombre = input("Ingrese el nombre de la ley que le interesa ver: \n")
    Ob.search_nombres(Nombre)
elif Opcion == "5":
    Ob.update_ley()
elif Opcion == "4":
    numero = int(input("PON EL NUMERO DE LA LEY: \n"))
    Ob.delete_ley(numero)
elif Opcion == "3":
    agregarNumberLey = int(input("Ingrese el numero de la ley que desea agregar:"))
    agregarNombreLey = input("Ingrese el nombre de esa ley")
    ley_Añadida = (agregarNombreLey)
    Ob.new_ley(ley_Añadida)

    
    
    
        

# leyxName1 = "Regimen legal del contrato del teletrabajo"
# leyxName2 = "Ley de contrato de trabajo"
# leyxName3 = "Ley de ejercicio profesional"
# N_ley1 = 27555
# N_ley2 = 20744
# N_ley3 = 7642
#solucionar la respuesta que debe enviar el SQL al usuario






