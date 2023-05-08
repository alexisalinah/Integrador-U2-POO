from ClaseAlumno import Alumno
import numpy as np
import csv
import ManejadorMaterias
class ManejadorAlumnos:
    def __init__(self):
        self.alumnos = np.array([], dtype=object)
        
    def cargar_datos(self, archivo_alumnos):
        with open(archivo_alumnos, 'r') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                dni = int(fila[0])
                apellido = fila[1]
                nombre = fila[2]
                carrera = fila[3]
                año = int(fila[4])
                alumno = Alumno(dni, apellido, nombre, carrera, año)
                self.alumnos = np.append(self.alumnos, alumno)
    def buscar_alumno_por_dni(self, dni):
            for alumno in self.alumnos:
                if alumno.dni == dni:
                    return alumno
            return None
        
    def calcular_promedio(self, dni):
        alumno = self.buscar_alumno_por_dni(dni)
        if alumno is None:
            return None
        materias_aprobadas = ManejadorMaterias.obtener_materias_aprobadas_por_alumno(dni)
        if len(materias_aprobadas) == 0:
            return None
        promedio = sum(materia.nota for materia in materias_aprobadas) / len(materias_aprobadas)
        promedio_con_aplazos = sum(materia.nota for materia in materias_aprobadas) / len(materias_aprobadas)
        return promedio, promedio_con_aplazos