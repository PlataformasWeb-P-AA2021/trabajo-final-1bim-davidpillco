from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Provincia
from configuracion import cadena_base_datos

import itertools

engine = create_engine('sqlite:///instituciones.db')

Session = sessionmaker(bind=engine)
session = Session()

# se crean objetos de tipo provincia

# leer el archivo de datos
provincias = open("data/Listado-Instituciones-Educativas.csv", "r",encoding='utf-8')
# Crear la lista vacia
unicos = []
# Ciclo para tratar los datos
for d in itertools.islice(provincias, 1, None):
    # Split para separacion de los datos
    cadena = d.split("|")
    a = cadena[len(cadena)-1].split("\n")
    cadena[len(cadena)-1] = a[0]
    # Creacion de las tuplas con el código y la provincia
    unicos.append((cadena[2],cadena[3]))
# Sacar los unicos de las tuplas
unicos=list(set(tuple(unicos)))
# Enviar los datos a la base
for x in unicos:
    mis_provincias = Provincia(codigo_provincia = x[0], provincia = x[1])
    session.add(mis_provincias)

# Guardar cambios
session.commit()