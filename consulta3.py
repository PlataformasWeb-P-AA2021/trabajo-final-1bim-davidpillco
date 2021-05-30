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

# Los cantones que tiene establecimientos con 0 número de profesores

consulta5 = session.query(Institucion).filter(Institucion.num_docentes == 0).all()
print(consulta5)

# Los establecimientos que pertenecen a la parroquia Catacocha con estudiantes mayores o iguales a 21

consulta6 = session.query(Institucion).join(Parroquia).filter(and_(Institucion.num_estudiantes >= 21,
Parroquia.parroquia == "CATACOCHA")).all()
print(consulta6)
