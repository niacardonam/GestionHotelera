# Clase por Diego Valle y Camilo Ramirez
# Se importan las clases necesarias para el correcto funcionamiento de la clase Hostales
from ClaseHabitacion import Habitacion
from ClaseValidaciones import Validador
import numpy as np


# Esta clase representa al objeto hostal 

class Hostales:
    # Variable que almacena el nombre del hostal
    nombre = str
    # Variable que almacena la direccion del hostal
    direccion = str
    # Variable que almacena el número de habitaciones del hostal
    numero_habitaciones = int
    # Variable que almacena la lista de servicios disponibles
    lista_servicios_disponibles = str
    # Variable que cuenta la cantidad de habitaciones registradas
    cont_habitaciones = int
    # Arreglo que almacena los objetos de tipo Habitacion creados
    habitaciones = np.ndarray
    # Variable que cuenta el número de incidentes registrados
    contador_incidentes = int
    # Arreglo que almacena los objetos de tipo Incidente registrados
    incidentes = np.ndarray
    # Constante que muestra la cantidad maxima de habitaciones que se puede registrar
    MAX_HABITACIONES = int

# Constructor de la clase Hostales
    def __init__(self):
        # Se inicializa la variable nombre como una cadena de texto vacia 
        self.nombre = ""
        # Se inicializa la variable direccion como una cadena de texto vacia 
        self.direccion = "" 
        # Se inicializa la vaiable número_habitaciones en 0
        self.numero_habitaciones = 0
        # Se inicializa la variable lista_servicios_disponibles como una cadena de texto vacia 
        self.lista_servicios_disponibles = ""
        # Se inicializa el contador de habitaciones en 0
        self.cont_habitaciones = 0
        # Se iniciliza la constante MAX_HABITACIONES en 10
        self.MAX_HABITACIONES = 10
        # Se inicializa el arreglo habitaciones con el valor None en todas sus casillas
        self.habitaciones=np.full((self.MAX_HABITACIONES), fill_value=None, dtype=object)

# Metodo que crea un Hostal
    def crear_hostal(self):
        # Variable de control del ciclo mientras incializada como True
        kiki = True
        # Se reescribe la variable nombre con el nombre ingresado por el usuario
        self.nombre = input("Ingrese el nombre del nuevo hostal: ")
        # Se reescribe la variable direccion con la dirección ingresada por el usuario
        self.direccion = input("Ingrese la dirección del nuevo hostal: ")
        # Ciclo mientras que verifica que el número de habitaciones ingresado por el usuario sea correcto
        while kiki:
            # Se utiliza el try-except para verificar que el dato ingresado sea un número entero
            try:
                # Se pide al usuario el número de habitaciones que tendra el hostal que esta registrando
                self.numero_habitaciones = int(input("Ingrese el número de habitaciones que tiene el nuevo hostal: "))
                # Condicional que verifica que el número ingresado sea mayor o igual a 1
                if(self.numero_habitaciones < 1):
                    print("Error: El número minimo de habitaciones que puede tener el hostal es 1")
                # Condicional que verifica que el número ingresado sea menor o igual a 10
                elif(self.numero_habitaciones > 10):
                    print("Error: El número maximo de habitaciones que puede tener el hostal es 10")
                else:
                    # Condicional que cambia el valor de kiki a False y cierra el ciclo
                    kiki = False
            except ValueError:
                print("Error: Valor incorreto, ingrese un número")
        # Variable de control del ciclo mientras incializada como True
        kiki = True
        # Ciclo mientras con el que se ingresan los servicios disponibles al hostal que esta registrando
        while kiki:
            # Variable que almacena la lista de servicios disponibles ingresados por el usuario
            self.lista_servicios_disponibles = input("Ingrese los servicios con los que contara el nuevo hostal: \n")
            # Se agrega el servicio ingresado en la lista de servicios disponibles
            self.lista_servicios_disponibles += self.lista_servicios_disponibles
            # Ciclo mientras anidado que verifica si el usuario quiere seguir ingresando servicios disponibles
            while kiki:
                # Variable que almacena la opción selecciona por el usuario
                agregar = input("¿Desea agregar otro servicio?(Si/No) \n")
                # Se llama a la funcion lower para descapitalizar la opcion ingresada por el usuario
                agregar.lower()
                # Se evalua si la opción ingresada por el usuario es "si" en dado caso cierra el ciclo interno
                if(agregar == "si"):
                    break
                # Se evalua la opción ingresada por el usuario es "no" en dado caso cambia el valor de kiki a False lo que termina ambos ciclos
                elif(agregar == "no"):
                    input("Presione enter para continuar")
                    kiki = False
                # Se valida la opción ingresada por el usuario no es ni "si" ni "no" 
                elif(agregar != "si" and agregar != "no"):
                    # Se muestra un mensaje indicanle al usuario que la opción ingresada no se encuentra disponible
                    print("Error: Esa opción no se encuentra disponible.")

# Metodo que crea una habitación
    def crear_habitacion(self):
        # Variable que controla el ciclo mientras
        continuar="si"
        # Ciclo mientras 
        while continuar.lower()=="si":
            try: 
                # Variable bandera inicializada en False
                flag=False
                # Variable que almacena el numero de identificacion de la habitación ingresado por el usuario
                numero_identificador_habitacion=int(input("Ingrese el número de identifciación de la nueva habitación: "))
                if(numero_identificador_habitacion < 1):
                    print("Error: El valor ingresado debe ser un número entero positivo")
                # Ciclo para que verifica si la el indentificador ingresado pertenece a alguna habitación registrada   
                for i in range(self.cont_habitaciones):
                    if numero_identificador_habitacion==self.habitaciones[i].num_id_habitacion:
                        flag=True
                        break
                if flag:
                    # Mensaje que indica al usuario que ya hay una habitación registrada con ese número identificador
                    print("Ya hay una habitación registrada con ese identificador")
                else:
                    # Se crea un objeto de tipo habitacion() 
                    habitacion=Habitacion()
                    # Se reescribe el número identificador de la habitación con el ingresado por el usuario
                    habitacion.num_id_habitacion=numero_identificador_habitacion
                    # Se llama al metodo pedir.datos() para llenar y almacenar los datos de la nueva habitación
                    habitacion.pedir_datos()
                    # Se almacena la nueva habitación en el arreglo de objetos habitaciones
                    self.habitaciones[self.cont_habitaciones]=habitacion
                    # Se incrementa el contador de habitaciones para poder almacenar otro hostal en la siguiente posicion del arreglo de objetos
                    self.cont_habitaciones+=1
                # Se pregunta al usuario si desea registrar más habitaciones
                continuar=input("¿Desea registar otra habitacion?(si/no)")
            except ValueError:
                print("Error: El valor ingresado debe ser un número entero positivo")
        print("Se han registrado correctamente las habitaciones")


# Metodo que registra un incidente en una habitación
    def registrar_incidente_en_habitacion(self):
        print("Registrar Incidentes")
        # se crea un bjeto de tipo validador() para hacer validaciones
        val = Validador()
        # Variable que contrala el ciclo mientras
        añadir_incidente = "si"
        while añadir_incidente.lower() == "si":
            # Variable que almacena el identicador de habitación ingresado por el usuario
            id_habitacion = val.leer_entero_positivo("Ingrese el identificador de la habitación: ")
            # Variable de tipo bandera inicializada en False
            encontrada = False
            # Ciclo para que verifica si el identicador de habitación ingresado por el usuario se relaciona con alguna habitación existente
            for i in range(self.cont_habitaciones):
                if id_habitacion == self.habitaciones[i].num_id_habitacion:
                    self.habitaciones[i].registrar_incidentes()
                    encontrada = True
                    break
            # Condicional que evalua si no se encontro la habitación y muestra un mensaje al usuario
            if not encontrada:
                print("No se encontró una habitación con ese identificador.")
            añadir_incidente = input("¿Desea registrar un nuevo incidente? (si/no): ")
      

