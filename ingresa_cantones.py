from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Canton, Provincia
from configuracion import cadena_base_datos

import itertools

engine = create_engine('sqlite:///instituciones.db')

Session = sessionmaker(bind=engine)
session = Session()


# leer el archivo de datos
cantones = open("data/Listado-Instituciones-Educativas.csv", "r",encoding='utf-8')
# Crear la lista vacia
unicos = []
cadena = []
b = []
# Ciclo para tratar los datos
for d in itertools.islice(cantones, 1, None):
    # Split para separacion de los datos
    g = d.split("|")
    a = g[len(g)-1].split("\n")
    g[len(g)-1] = a[0]
    cadena.append(g)
    # Creacion de las tuplas con el código y la canton
    unicos.append((g[4],g[5],g[3]))
# Sacar los unicos de las tuplas
unicos=list(set(tuple(unicos)))
# print(unicos)
print(len(unicos))

# Obtencion de las provincia
provincias = session.query(Provincia).all()

#  Comparativa
for x in unicos:
    for i in provincias:
        if(x[2] == i.provincia):
            b.append(i.codigo_provincia)

# Enviar los datos a la base
cont = 0
for x in unicos:
    mis_cantones = Canton(codigo_canton = x[0], canton = x[1], id_provincia = b[cont])
    cont+= 1
    print(mis_cantones)
    session.add(mis_cantones)

# Guardar cambios
session.commit()