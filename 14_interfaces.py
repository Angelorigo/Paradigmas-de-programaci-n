#=============================================================
#  Del directorio aplicación, el subdirectorio repositorio, 
#  el archivos basededatos.py : trae el objeto Basededatos
#=============================================================

from aplicacion.repositorio.basededatos import BaseDeDatos


#============================================================
#  Del directorio aplicación, el subdirectorio repositorio,
#  el archivo s3.py : trae el objeto S3
#============================================================

from aplicacion.repositorio.s3 import S3


#======================================================================
#  Del directorio aplicación, el subdirectiorio repositorio,
#  el archivo sistemadearchivos.py : trae el objeto SistemaDeArchivos
#======================================================================

from aplicacion.repositorio.sistemadearchivos import SistemaDeArchivos


#========================================================
#  Del directorio aplicación, el subdirectorio modelos,
#  el archivo usuario.py : trae el objeto Usuario
#========================================================

from aplicaion.modelos.usuario import Usuario


#==============================================================================
#  Del directorio aplicación, el subdirectorio negocios,
#  el archivo manejodeinscripciones.py : trae el objeto ManejoDeInscripciones
#==============================================================================

from aplicacion.negocios.manejodeinscripciones import ManejoDeInscripciones


#==============================
#  Crear el objeto de Usuario
#==============================

usuario = Usuario("Roberto", "Jiménez", 18)


#======================
#  Crear el objeto s3  
#======================

repositorioS3 = S3("321321321", "sdf324223", "MiCubeta")


#===============================================================
#  Interfase inscribirUsuario del objeto ManejoDeInscripciones
#===============================================================

ManejoDeInscripciones.inscribirUsuario(usuario, repositorioS3)
print("\n")


#=====================================
#  Crear el objeto sistemadearchivos
#=====================================

repositorioSistemaDeArchivos = SistemaDeArchivos("/home/users")


#===============================================================
#  Interfase inscribirUsuario del objeto ManejoDeInscripciones
#===============================================================

ManejoDeInscripciones.inscribirUsuario(usuario, repositorioSistemaDeArchivos)
print("\n")


#===============================
#  Crear el objeto basededatos
#===============================

repositorioBaseDeDatos = BaseDeDatos("localhost", "admin", "admin123")


#===============================================================
#  Interfase inscribirUsuario del objeto ManejoDeInscripciones
#===============================================================

ManejoDeInscripciones.inscribirUsuario(usuario, repositorioBaseDeDatos)
print("\n")