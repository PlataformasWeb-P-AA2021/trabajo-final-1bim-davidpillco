from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Institucion, Parroquia , Canton , Provincia

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Consulta 1 Todos los establecimientos de la provincia de Loja.

consulta1 = session.query(Institucion).join(Parroquia,Canton,Provincia).filter(Provincia.provincia == 'LOJA').all()
print(consulta1)

# Todos los establecimientos del cantón de Loja.
consulta2 = session.query(Institucion).join(Parroquia,Canton,Provincia).filter(Canton.canton == 'LOJA').all()
print(consulta2)