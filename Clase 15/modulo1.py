class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


    def __str__(self):
        return f"NOMBRE {self.nombre}"

#OJO esto es el primer ejemplo, siempre es aconsejable que los 
#modulos y paquetes tengan nombres representativos