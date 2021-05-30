from ast import Str
from sqlalchemy import column, create_engine, false, null, true
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Base = declarative_base()

# Creacion de la clase institucion

class Institucion(Base):
    # Nombre de la tabla
    __tablename__ = 'institucion'
    # Llave primaria
    id = Column(Integer, primary_key=True)
    codigo = Column(String(100))
    nombre = Column(String(100))
    distrito = Column(String(100))
    sostenimiento = Column(String(100))
    tipo_educacion = Column(String(100))
    modalidad = Column(String(100))
    jornada = Column(String(100))
    acceso = Column(String(100))
    num_estudiantes = Column(Integer, nullable=False)
    num_docentes = Column(Integer, nullable=False)
    id_parroquia =  Column(String, ForeignKey('parroquia.codigo_parroquia'))
    parroquia = relationship("Parroquia", back_populates="instituciones")

    def __repr__(self):
        return "Institucion: codigo=%s nombre=%s Distrito=%s Sostenimiento =%s Tipo_educacion =%s Modalidad=%s Jornada=%s Acceso=%s Num_estudiantes =%d Num_docentes=%d id_parroquia=%s"%(
            self.codigo,
            self.nombre,
            self.distrito,
            self.sostenimiento,
            self.tipo_educacion,
            self.modalidad,
            self.jornada,
            self.acceso,
            self.num_estudiantes,
            self.num_docentes,
            self.id_parroquia
        )

# Creacion de la clase Parroquia

class Parroquia(Base):
    # Nombre de la tabla
    __tablename__ = 'parroquia'
    # Llave primaria
    id = Column(Integer, primary_key=True)
    codigo_parroquia = Column(String(100))
    parroquia = Column(String, nullable=False)
    instituciones = relationship("Institucion", back_populates="parroquia")
    id_canton = Column(String, ForeignKey('canton.codigo_canton'))
    canton = relationship("Canton", back_populates="parroquias")

    def __repr__(self):
        return "Parroquia: codigo=%s  Parroquia=%s id_canton = %s"%(
            self.codigo_parroquia,
            self.parroquia,
            self.id_canton
        )

# Creacion de la clase Canton
class Canton(Base):
    # Nombre de la tabla
    __tablename__ = 'canton'
    # Llave primaria
    id = Column(Integer, primary_key=True)
    codigo_canton = Column(String(100))
    canton = Column(String, nullable=False)
    parroquias = relationship("Parroquia", back_populates="canton")
    id_provincia = Column(String, ForeignKey('provincia.codigo_provincia'))
    provincia = relationship("Provincia", back_populates="cantones")

    def __repr__(self):
        return "Canton: codigo=%s Canton=%s id_provincia = %s"%(
            self.codigo_canton,
            self.canton,
            self.id_provincia
        )

# Creacion de la clase Provincia
class Provincia(Base):
    # Nombre de la tabla
    __tablename__ = 'provincia'
    # Llave primaria
    id = Column(Integer, primary_key=True)
    codigo_provincia = Column(String(100))
    provincia = Column(String, nullable=False)
    cantones = relationship("Canton", back_populates="provincia")

    def __repr__(self):
        return "Provincia: codigo=%s Provincia=%s"%(
            self.codigo_provincia,
            self.provincia
        )

Base.metadata.create_all(engine)