import csv
from ClaseMateriasAprobadas import MateriasAprobadas

class ManejadorMaterias:
    def __init__(self):
        self.materias = []
        
    def cargar_datos(self, archivo_materias):
        with open(archivo_materias, 'r') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                dni_alumno = int(fila[0])
                nombre_materia = fila[1]
                fecha = fila[2]
                nota = int(fila[3])
                aprobacion = fila[4]
                materia = materia(dni_alumno, nombre_materia, fecha, nota, aprobacion)
                self.materias.append(materia)
                
    ##@classmethod
    ##def obtener_materias_aprobadas_por_alumno(cls, dni_alumno)