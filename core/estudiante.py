import re

class estudiante:
    def __init__(self, id, nombre, a_paterno, a_materno, dni, fecha_nacimiento, sexo, email, celular):
        self.__id = id
        self.__nombre = nombre
        self.__a_paterno = a_paterno
        self.__a_materno = a_materno
        self.__dni = dni
        self.__fecha_nacimiento = fecha_nacimiento
        self.__sexo = sexo
        self.__cursos = []
        self.__asistencias = []
        self.__email = email
        self.__celular = celular

    #GETTERS Y SETTERS
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, valor):
        self.__id = valor
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor
    
    @property
    def a_paterno(self):
        return self.__a_paterno
    
    @a_paterno.setter
    def a_paterno(self, valor):
        self.__a_paterno = valor

    @property
    def a_materno(self):
        return self.__a_materno
    
    @a_materno.setter
    def a_materno(self, valor):
        self.__a_materno = valor

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, valor):
        self.__dni = valor

    @property
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento
    
    @fecha_nacimiento.setter
    def fecha_nacimiento(self, valor):
        self.__fecha_nacimiento = valor
    
    @property
    def sexo(self):
        return self.__sexo
    
    @sexo.setter
    def sexo(self, valor):
        self.__sexo = valor

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, valor):
        self.__email = valor

    @property
    def celular(self):
        return self.__celular
    
    @celular.setter
    def celular(self, valor):
        self.__celular = valor
    
    @property
    def cursos(self):
        return self.__cursos
    
    @property
    def asistencias(self):
        return self.__asistencias
    
