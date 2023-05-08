class MateriasAprobadas:
    __dni=''
    __NombreMateria=''
    __fecha=''
    __nota=0
    __aprobacion=''
    def __init__(self, dni, nombremateria, fecha, nota, aprobacion):
        self.__dni =  dni
        self.__NombreMateria = nombremateria
        self.__fecha= fecha
        self.__nota=nota
        self.__aprobacion=aprobacion
        