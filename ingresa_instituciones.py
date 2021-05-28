from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Provincia, Institucion
from configuracion import cadena_base_datos

import itertools

engine = create_engine('sqlite:///instituciones.db')

Session = sessionmaker(bind=engine)
session = Session()

# se crean objetos de tipo provincia

# leer el archivo de datos
instituciones = open("data/Listado-Instituciones-Educativas.csv", "r",encoding='utf-8')
# Crear la lista vacia
unicos = []
# Ciclo para tratar los datos
for d in itertools.islice(instituciones, 1, None):
    cadena = d.split("|")
    a = cadena[len(cadena)-1].split("\n")
    cadena[len(cadena)-1] = a[0]
    mis_instituciones = Institucion(codigo = cadena[0],nombre=cadena[1], distrito = cadena[8], sostenimiento = cadena[9],\
        tipo_educacion = cadena[10], modalidad = cadena[11], jornada = cadena[12], acceso = cadena[13],\
        num_estudiantes = cadena[14], num_docentes = cadena[15])
    print(mis_instituciones)