from aplicacion.modelos.usuario import Usuario
from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios


#===============================
#  Clase ManejoDeInscripciones
#  NO TIENE VARIABLES!!!
#===============================

class ManejoDeInscripciones:
    
    
    #================================================================== 
    #  Decorador staticmethod
    #  El objeto sólo tiene la función inscribirUsuario
    #  ENVUELVE LA FUNCIÓN SIN LLAMAR VARIABLES LOCALES
    #  El objeto ManejoDeInscripciones es la interfase intercambiable
    #==================================================================
    
    @staticmethod
    def inscribirUsuario(usuario: Usuario, repositorioDeUsuarios: RepositorioDeUsuarios) -> None:
        print("-------> Guardando usuario... \n")
        repositorioDeUsuarios.abrir()
        repositorioDeUsuarios.guardar(usuario)
        repositorioDeUsuarios.cerrar()