# Clase por Camilo Ramirez, Diego Valle, Estefania Cardona
# Se importan las clases necesarias para el correcto funcionamiento de la clase menu
from ClaseHostales import Hostales
from ClaseUsuario import Usuario
from ClaseHabitacion import Habitacion
import numpy as np

# Esta clase representa el menu principal y se encarga de almacenar y procesar los objetos creados

class AppMenu:
    # Contador que muestra la cantidad de usuarios registrados
    contador_usuarios = int
    # Contador que muestra la cantidad de hostales registrados
    contador_hostales = int
    # Constante que muestra la cantidad maxima de usuarios que se puede agregar
    MAXIMO_USUARIO = int
    # Constante que muestra la cantidad maxima de hostasles que se puede registrar
    MAXIMO_HOSTALES = int
    # Arreglo en el que se almacenan los objetos de tipo Usuario creados
    usuarios = np.ndarray
    # Arreglo que almacena los objetos de tipo hostales creados
    hostales = np.ndarray

# Se crea el metodo constructor para inicializar las variables
    def __init__(self):
        # Se inicializa el contador del número de usuarios en 0
        self.contador_usuarios = 0
        # Se inicializa el contador del número de hostales en 0
        self.contador_hostales = 0
        # Se inicializa la constante MAXIMO_USUARIOS en 20 
        self.MAXIMO_USUARIO = 20
        # Se inicializa la constante MAXIMO_HOSTALES en 5
        self.MAXIMO_HOSTALES = 5
        # Se inicializa el arreglo  usuarios con el valor None en todas sus casillas
        self.usuarios = np.full ((self.MAXIMO_USUARIO), fill_value = None, dtype=object)
        # Se inicializa el arreglo hostales con el valor None en todas sus casillas
        self.hostales = np.full ((self.MAXIMO_HOSTALES), fill_value = None, dtype=object)

# Se crea el metodo menu para acceder a las funciones que ofrece el programa   
    def menu(self):
        # Variable de control para el ciclo del menu, inicializada en 0
        menu = int
        menu = 0
        # Ciclo que muestra el menu y sus opciones
        while menu!=5:
            # Se utiliza el try-except para verificar que el dato ingresado sea un numero entero
            try:
                print("************** MENU **************")
                # se muestran las opciones con las que cuenta el menu
                menu = int(input("Seleccione que desea hacer: \n1. Registrar un Usuario \n2. Registrar un Hostal \n3. Registrar una Habitación \n4. Registrar un Incidente \n5. Salir\n**********************************\n"))
                # Condicional que verifica que el número ingresado se encuentre en el rango
                if(menu > 5 or menu < 1):
                    print("Error: La opcion que seleciono no se encuentra disponible")
                    input("Presioner enter tecla para continuar")
            except ValueError:
                # Mensaje que le indica al usuario que el valor ingresado es incorrecto
                print("Error: La opción seleccionada debe ser un número entre 1 y 5")
                input("Presione enter tecla para continuar")
    
            match menu:
                # Al seleccionar la opcion 1 el programa le permite al usuario registrar un nuevo usuario
                case 1:
                    # Se crea un objeto de tipo Usuario 
                    nuevo_usuario = Usuario()
                    # Se llama a la funcion crear_usuario() para registrar el nuevo usuario
                    nuevo_usuario.crear_usuario()
                    # Se almacena el nuevo usuario en el arreglo de objetos usuario
                    self.usuarios[self.contador_usuarios] = nuevo_usuario
                    # Se incrementa el contador de usuarios para poder almacenar otro usuario en la siguiente posicion del arreglo de objetos
                    self.contador_usuarios += 1
                # Al selecionar la opcion 2 el programa le permite al usuario registrar un hostal
                case 2:
                    # Se crea un objeto de tipo Hostal 
                    nuevo_hostal = Hostales()
                    # Se llama a la funcion crear_hostal() para registrar el nuevo hostal
                    nuevo_hostal.crear_hostal()
                    # Se almacena el nuevo hostal en el arreglo de objetos hostales
                    self.hostales[self.contador_hostales] = nuevo_hostal
                    # Se incrementa el contador de hostales para poder almacenar otro hostal en la siguiente posicion del arreglo de objetos
                    self.contador_hostales += 1
                    # Se muestra un mensaje que indique al usuario que se ha creado el hostal correctamente
                    input("Hostal registrado correctamente. \nPresione enter para continuar")
                # Al seleccionar la opcion 3 el programa le permite al usuario registrar una habitación
                case 3:
                    # Condicional que evalua si hay hostales creados
                    if self.contador_hostales == 0:
                        # Mensaje que indica al usuario que no hay hostales registrados
                        print("Error: No hay hostales registrados para agregar una habitación.")
                        input("Presione enter para continuar.")
                    else:                       
                        print("Lista de hostales disponibles:")
                        # ciclo que muestra al usuario la lista de hostales disponibles
                        for i in range(self.contador_hostales):
                            print(f"{i + 1}. {self.hostales[i].nombre}")  
                    # Se utiliza el try-except para verificar que el dato ingresado sea un numero entero
                    try:
                        # Se crea la varible opción que almacena el número selecionado por el usuario
                        opcion = int(input("Seleccione el número del hostal al que desea agregar la habitación: "))
                        # Se verifica que la opcion selecionada se encuentre en el rango
                        if opcion  >= 1 and opcion <= self.contador_hostales:
                            # Se llama la funcion crear_habitacion() desde el arreglo hostales para almacenar la nueva habitación
                            self.hostales[opcion - 1].crear_habitacion()
                            # Se muestra un mensaje indicando al usuario que la habitacion se creo correctamente
                            input("Habitación registrada correctamente.\nPresione enter para continuar.")

                        else:
                            # Se muestra un mensaje que indica al usuario que la opción seleccionada no se encuectra disponible
                            print("Error: Opción inválida.")
                            input("Presione enter para continuar.")
                    except ValueError:
                        print("Error: Ingrese un número válido.")
                        input("Presione enter para continuar.")
                # Al seleccionar la opcion 4 el programa le permite al usuario registrar un incidente en una habitación   
                case 4:
                    # Condicional que evalua si hay hostales creados
                    if self.contador_hostales == 0:
                        # Mensaje que indica al usuario que no hay hostales registrados
                        print("Error: No hay hostales registrados para registrar un incidente.")
                        input("Presione enter para continuar.")
                    else:
                        print("Lista de hostales disponibles:")
                         # ciclo que muestra al usuario la lista de hostales disponibles
                        for i in range(self.contador_hostales):
                            print(f"{i + 1}. {self.hostales[i].nombre}")
                        # Se utiliza el try-except para verificar que el dato ingresado sea un numero entero
                        try:
                            # Se crea la varible opción que almacena el número selecionado por el usuario
                            opcion = int(input("Seleccione el número del hostal donde desea registrar el incidente: "))
                            # Se verifica que la opcion selecionada se encuentre en el rango
                            if (opcion  >= 1 and opcion <= self.contador_hostales):
                                # Se llama la funcion registrar_incidente_en_habitacion() desde el arreglo hostales para registrar el incidente
                                self.hostales[opcion - 1].registrar_incidente_en_habitacion()
                            else:
                                # Se muestra un mensaje que indica al usuario que la opción seleccionada no se encuectra disponible
                                print("Error: Opción inválida.")
                                input("Presione enter para continuar.")
                        except ValueError:
                            print("Error: Ingrese un número válido.")
                            input("Presione enter para continuar.") 
                # Al seleccionar la opcion 4 el programa le permite al usuario terminar el programa
                case 5:
                    print("Adios")
                    break  

                


                    
    
obj = AppMenu()
obj.menu()

