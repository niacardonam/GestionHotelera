# Clase por Diego Valle, Estefania Cardona, Camilo Ramirez
# Se crea una clase llamada Validador que contiene métodos para validar entradas del usuario.
class Validador:
    # Este metodo solicita un número entero positivo al usuario y lo devuelve.
    def leer_entero_positivo(self, mensaje):
        # Se crea un ciclo para pedir al usuario un número hasta que se ingrese uno válido.
        while True:
            # Se maneja una excepción para capturar errores de entrada.
            try:
                # Se solicita al usuario un número entero positivo.
                numero = int(input(mensaje))
                # Se verifica si el número es positivo.
                if numero >= 0:
                    # Si es positivo, se devuelve el número.
                    return numero
                # Si no es positivo, se muestra un mensaje de error.
                else:
                    print("Debe ser un número entero positivo.")

            # Si no se ingrese un carácter válido, se captura la excepción y se muestra un mensaje de error.
            except:
                print("Error: debe ingresar un número entero.")
    # Este método solicita un número decimal positivo al usuario y lo devuelve.
    def leer_real_positivo(self, mensaje):
        # Se crea un ciclo para pedir al usuario un número hasta que se ingrese uno válido.
        while True:
            # Se maneja una excepción para capturar errores de entrada.
            try:
                # Se solicita al usuario un número decimal positivo.
                numero = float(input(mensaje))
                # Se verifica si el número es positivo.
                if numero >= 0:
                    # Si es positivo, se devuelve el número.
                    return numero
                # Si no es positivo, se muestra un mensaje de error.
                else:
                    print("Debe ser un número positivo.")
            except:
                # Si no se ingrese un carácter válido, se captura la excepción y se muestra un mensaje de error.
                print("Error: debe ingresar un número decimal válido.")
    # Este método solicita una opción de menú al usuario y la valida dentro de un rango específico.
    def leer_opcion_menu(self, mensaje, minimo, maximo):
        # Se crea un ciclo para pedir al usuario una opción hasta que se ingrese una válida.
        while True:
            # Se maneja una excepción para capturar errores de entrada.
            try:
                # Se solicita al usuario una opción de menú.
                opcion = int(input(mensaje))
                # Se verifica si la opción está dentro del rango especificado.
                if opcion >= minimo and opcion <= maximo:
                    # Si es válida, se devuelve la opción.
                    return opcion
                # Si no está dentro del rango, se muestra un mensaje de error.
                else:
                    # Se informa al usuario del rango válido.
                    print(f"Seleccione un número entre {minimo} y {maximo}.")
            # Si no se ingrese un carácter válido, se captura la excepción y se muestra un mensaje de error.
            except:
                print("Error: debe ingresar un número entero.")
                
                