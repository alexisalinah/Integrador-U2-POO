class Alumno:
    __dni=''
    __apellido=''
    __nombre=''
    __carrera=''
    __anio_cursa=''
    def __init__(self, dni, apellido, nombre, carrera, aniocursa):
        self.__dni=dni
        self.__apellido=apellido
        self.__nombre=nombre
        self.__carrera=carrera
        self.__anio_cursa=aniocursa