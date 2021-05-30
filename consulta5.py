from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and y or

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

# Los establecimientos ordenados por nombre de parroquia que tengan más de 20 profesores y la cadena "Permanente" en tipo de educación.
print("Consulta 9")
consulta9 = session.query(Institucion).join(Parroquia).filter(and_(Institucion.num_docentes > 20,
Institucion.tipo_educacion.like("%Permanente%"))).order_by(Parroquia.parroquia).all()
# Impresión consulta
print(consulta9)
print("------------------------")
print("Consulta 10")
# Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D02.

consulta10 = session.query(Institucion).join(Parroquia).filter(Institucion.distrito == '11D02').order_by(Institucion.sostenimiento).all()
# Impresión consulta
print(consulta10)
