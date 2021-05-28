from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Canton, Provincia, Parroquia
from configuracion import cadena_base_datos

import itertools

engine = create_engine('sqlite:///instituciones.db')

Session = sessionmaker(bind=engine)
session = Session()


# leer el archivo de datos
parroquia = open("data/Listado-Instituciones-Educativas.csv", "r",encoding='utf-8')
# Crear la lista vacia
unicos = []
cadena = []
b = []
# Ciclo para tratar los datos
for d in itertools.islice(parroquia, 1, None):
    g = d.split("|")
    a = g[len(g)-1].split("\n")
    g[len(g)-1] = a[0]
    cadena.append(g)
    # Creacion de las tuplas con el código y la canton
    unicos.append((g[6],g[7],g[5]))
# Sacar los unicos de las tuplas
unicos=list(set(tuple(unicos)))
# Obtencion de los cantones
cantones = session.query(Canton).all()
#  Comparativa
for x in unicos:
    for i in cantones:
        if(x[2] == i.canton):
            b.append(i.codigo_canton)
# Enviar los datos a la base
cont = 0
for x in unicos:
    mis_parroquias = Parroquia(codigo_parroquia = x[0], parroquia = x[1], id_canton = b[cont])
    cont+= 1
    print(mis_parroquias)
    session.add(mis_parroquias)

session.commit()
