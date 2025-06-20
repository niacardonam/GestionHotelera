# Clase por Diego Valle
# se debe importar las clases que se utilizaran en el codigo
from ClaseIncidentes import Incidente
from ClaseValidaciones import Validador
# se importa la libreria numpy para manejar arreglos
import numpy as np
# Se crea la clase Habitacion, la cual representa una habitacion de un hotel
class Habitacion:
    # Se definen los atributos de la clase Habitacion
    tipo_habitacion= int
    num_id_habitacion= int
    tarifa_noche= float
    estado= int
    descripcion= str
    # Se crea un arreglo de objetos Incidente para almacenar los incidentes de la habitacion
    lista_incidentes= np.ndarray
    # Se define un contador para llevar el registro de los incidentes
    cont_incidentes= int

# Se crea un metodo constructor, el cual inicializa los valores de los atributos
    def __init__(self):
        # Inicializa los atributos de la clase Habitacion
        self.tipo_habitacion= 0
        self.num_id_habitacion= 0
        self.tarifa_noche= 0
        self.estado= 0
        self.descripcion= ""
        # Inicializa un arreglo de objetos Incidente con un tamaño fijo de 100
        self.lista_incidentes= np.full((100), fill_value=None, dtype=object)
        # Inicializa el contador de incidentes a 0, el cual se utilza para establecer la posicion en el arreglo de incidentes
        self.cont_incidentes= 0

# Se crea un metodo para pedir los datos de la habitacion
    def pedir_datos(self):
        # Se crea un objeto Validador para validar los datos ingresados por el usuario
        val = Validador()
        # Se solicita al usuario que ingrese los datos de la habitacion
        self.tipo_habitacion = val.leer_opcion_menu("Ingrese el tipo de habitacion (1. Sencilla, 2. Doble, 3. Suite ): ", 1, 3)
        self.tarifa_noche = val.leer_real_positivo("Ingrese la tarifa por noche: ")
        self.estado = val.leer_opcion_menu("Ingrese el estado de la habitación (1. Disponible, 2. Ocupada, 3. Fuera de servicio): ", 1, 3)
        self.descripcion = input("Ingrese la descripción de la habitacion: ")
        
# Se crea un metodo para registar incidentes por cada habitacion
    def registrar_incidentes(self):
        # Se crea un objeto Validador para validar los datos ingresados por el usuario
        val = Validador()
        # Se crea una varible para controlar el ciclo que registra los incidentes
        continuar = "si"
        # Se crea un ciclo que se ejecuta mientras el usuario desee registrar incidentes
        while continuar.lower() == "si":
            print("\n-------- Tipo de incidente --------")
            print(" 1. Mantenimiento\n 2. Limpieza\n 3. Otro")
            # Se registra y se valida el tipo de incidente
            tipo_incidente = val.leer_opcion_menu("Seleccione el tipo de incidente (1-3): ", 1, 3)

            print("\n-------- Estado --------")
            print(" 1. Pendiente\n 2. En Proceso\n 3. Resuelto")
            # Se registra y se valida el estado del incidente
            estado = val.leer_opcion_menu("Seleccione el estado en el que se encuentra el incidente (1-3): ", 1, 3)
            # Se registra la fecha del incidente
            fecha_registro = input("Ingrese la fecha (ejemplo: 2025-05-31): ")
            # Se crea un obejto de tipo incidente el cual contiene los datos registrados previamente
            inc = Incidente()
            # Se añade el obejeto anterior al arreglo que guarda los incidentes por habitacion
            self.lista_incidentes[self.cont_incidentes] = inc
            # Se incremente el contador, para guardar un nuevo incidente en una nueva posición del arreglo
            self.cont_incidentes += 1
            #Cambiamos el valor de la variable que controla el ciclo para verificar si el usuario desea registrar otro incidente
            continuar = input("¿Desea registrar otro incidente para esta habitación? (si/no): ")
        # Se imprime un mensaje de confirmación al finalizar el registro de incidentes
        print("Incidentes registrados correctamente.")

