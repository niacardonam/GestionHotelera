# Clase por Diego
# Esta clase representa el objeto incidente 
class Incidente:
    # Variable que almacena el numero identificador de la habitación a la que pertenece el incidente registrado
    numero_identificador_habitacion= int
    # Variable que almacena el tipo de incidente a registrar (1 = Mantenimiento 2 = Limpieza 3 = Otro)
    tipo_incidente= int
    # Variable que almacena el estado en el que se encuentra el incidente (1 = Pendiente 2 = En Proceso 3 = Resuelto)
    estado= int
    # Variable que almacena la fecha del registro del incidente (En formato 0000-00-00)
    fecha_registro= str
    # Variable que almacena la fecha en la que se soluciono el incidente (En formato 0000-00-00)
    fecha_solucion= str

# Se crea un metodo constructor, el cual inicializa los valores de los atributos
    def _init_(self, numero_identificador_habitacion, tipo_incidente, estado, fecha_registro, fecha_solucion):
        self.numero_identificador_habitacion= numero_identificador_habitacion
        self.tipo_incidente= tipo_incidente
        self.estado = estado
        self.fecha_registro= fecha_registro
        self.fecha_solucion=fecha_solucion