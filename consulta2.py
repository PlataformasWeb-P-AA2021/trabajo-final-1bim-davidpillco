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

# Las parroquias que tienen establecimientos únicamente en la jornada Nocturna

consulta3 = session.query(Parroquia).join(Institucion).filter(Institucion.jornada == 'Nocturna').all()
print(consulta3)

# Los cantones que tiene establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459

consulta4 = session.query(Canton).join(Parroquia,Institucion).filter(or_(Institucion.num_estudiantes == 448,Institucion.num_estudiantes==450,
    Institucion.num_estudiantes==451, Institucion.num_estudiantes==454, Institucion.num_estudiantes == 458, Institucion.num_estudiantes == 459)).all()
print(consulta4)
