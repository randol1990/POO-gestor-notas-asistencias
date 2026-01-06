#Clase Estudiante: hereda de la clase Persona  id, nombre, a_paterno, a_materno, dni, fecha_nacimiento, sexo, email, celular

from persona import Persona

class Estudiante(Persona):
    def __init__(self, id, nombre, a_paterno, a_materno, dni, fecha_nacimiento, sexo, email, celular):
        super().__init__( id, nombre, a_paterno, a_materno, dni, fecha_nacimiento, sexo, email, celular)
        self.__cursos = []
        self.__asistencias = []

    #GETTERS Y SETTERS
    @property
    def cursos(self):
        return self.__cursos
    
    @property
    def asistencias(self):
        return self.__asistencias
    
