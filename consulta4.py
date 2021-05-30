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

# Los establecimientos ordenados por número de estudiantes; que tengan más de 100 estudiantes.

consulta7 = session.query(Institucion).filter(Institucion.num_docentes > 100).order_by(Institucion.num_estudiantes).all()
print(consulta7)

# Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores.

consulta8 = session.query(Institucion).filter(Institucion.num_docentes > 100).order_by(Institucion.num_docentes).all()
print(consulta8)
