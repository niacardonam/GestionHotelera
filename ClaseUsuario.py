# Clase por Camilo Ramirez
# Se importa la libreria numpy para el manejo de arreglos
import numpy as np
# Se crea la clase usuario
class Usuario:
    # Se definen los atributos de la clase Usuario
    tipo_usuario = int
    nombre = str
    documento = str
    correo = str
    direccion = str
    telefono = str
   
# Constructor de la clase Usuario
    def __init__(self):
        # Se inicializan los atributos de la clase Usuario
        self.tipo_usuario = 0
        self.nombre = ""
        self.documento = ""
        self.correo = ""
        self.direccion = ""
        self.telefono = ""
# Metodo que crea un usuario
    def crear_usuario(self):
        # Se crea una variable bandera para controlar el bucle
        kiki = True
        # Se inicia un bucle que se ejecuta hasta que se cree un usuario correctamente
        while kiki:
            # Se registra la información del usuario
            # Se verifica que se ingresen valores válidos para el tipo de usuario
            try:
                self.tipo_usuario = int(input("Seleccione el tipo de usuario que desea crear: \n 1. Cliente \n 2. Recepcionista \n 3. Administrador \n "))
                # Se verifica que el tipo de usuario esté dentro del rango permitido
                if(self.tipo_usuario < 1 or self.tipo_usuario > 3):
                    # Si el tipo de usuario no es válido, se muestra un mensaje de error
                    # y se solicita nuevamente la información
                    print("Error: Esa opción no se encuentra disponible")
                # Si el tipo de usuario es válido, se solicita la información correspondiente dependiendo del tipo de usuario
                # si el tipo de usuario es 1, se solicita la información del cliente
                elif(self.tipo_usuario == 1):
                    self.nombre = input("Ingrese el nombre del cliente: ")
                    self.documento = input("Ingrese el número de documento del cliente: ")
                    self.correo = input("Ingrese la dirección de correo electronico del cliente: ")
                    self.direccion = input("Ingrese la dirección de residencia del cliente: ")
                    self.telefono = input("Ingrese el número telefónico del cliente: ")
                    input("Cliente registrado correctamente \nPresione cualquier tecla para continuar")
                    # Se cambia la variable bandera a False para salir del bucle
                    kiki = False
                # si el tipo de usuario es 2, se solicita la información del recepcionista
                elif(self.tipo_usuario == 2):
                    self.nombre = input("Ingrese el nombre de él nuevo recepcionista: ")
                    self.documento = input("Ingrese el número de documento de él nuevo recepcionista: ")
                    self.correo = input("Ingrese la dirección de correo electronico de él nuevo recepcionista: ")
                    self.direccion = input("Ingrese la dirección de residencia de él nuevo recepcionista: ")
                    self.telefono = input("Ingrese el número telefónico de él nuevo recepcionista: ")
                    input("Recepcionista registrado correctamente \nPresione cualquier tecla para continuar")
                    # Se cambia la variable bandera a False para salir del bucle
                    kiki = False
                # si el tipo de usuario es 3, se solicita la información del administrador
                elif(self.tipo_usuario == 3):
                    self.nombre = input("Ingrese el nombre de él nuevo Administrador: ")
                    self.documento = input("Ingrese el número de documento de él nuevo Administrador: ")
                    self.correo = input("Ingrese la dirección de correo electronico de él nuevo Administrador: ")
                    self.direccion = input("Ingrese la dirección de residencia de él nuevo Administrador: ")
                    self.telefono = input("Ingrese el número telefónico de él nuevo Administrador: ")
                    input("Administrador registrado correctamente \nPresione cualquier tecla para continuar")
                    # Se cambia la variable bandera a False para salir del bucle
                    kiki = False    
            # Si se ingresa un valor no numérico para el tipo de usuario, se captura la excepción
            except ValueError:
                # Se muestra un mensaje de error indicando que la opción debe ser un número entre 1 y 3
                print("Error: La opción seleccionada debe ser un número entre 1 y 3")

                    
                        


