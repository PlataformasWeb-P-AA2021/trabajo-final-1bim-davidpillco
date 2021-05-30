from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Provincia, Institucion, Parroquia
from configuracion import cadena_base_datos

import itertools

engine = create_engine('sqlite:///instituciones.db')

Session = sessionmaker(bind=engine)
session = Session()

# leer el archivo de datos
instituciones = open("data/Listado-Instituciones-Educativas.csv", "r",encoding='utf-8')

#  Obtencion de  parroquias
parroquias = session.query(Parroquia).all()
# Ciclo para tratar los datos
for d in itertools.islice(instituciones, 1, None):
    # Split para separacion de los datos
    cadena = d.split("|")
    a = cadena[len(cadena)-1].split("\n")
    cadena[len(cadena)-1] = a[0]
    # Comparativa para asignar cada id_provincia
    for i in parroquias:
        if(cadena[7] == i.parroquia):
            cod = i.codigo_parroquia

    # Ingreso de los datos
    mis_instituciones = Institucion(codigo = cadena[0],nombre=cadena[1], distrito = cadena[8], sostenimiento = cadena[9],\
    tipo_educacion = cadena[10], modalidad = cadena[11], jornada = cadena[12], acceso = cadena[13],\
    num_estudiantes = int(cadena[14]),num_docentes = int(cadena[15]), id_parroquia = cod)

    session.add(mis_instituciones)
# Guardar cambios
session.commit()

