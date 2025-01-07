from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios
from aplicacion.modelos.usuario import usuario


#=======================================
#  S3 es hijo de RepositorioDeUsuarios
#=======================================

class S3(RepositorioDeUsuarios):
    __clientID: str
    __secretKey: str
    __bucket: str
    
    def __init__(mi, clientID: str, secretKey: str, bucket: str):
        mi.__clientID = clientID
        mi.__secretKey = secretKey
        mi.__bucket = bucket
        
    def abrir(mi) -> None:
        print(f"Estableciendo conexión a AWS S3 {mi.__clientID}:{mi.__secretKey}")
    
    def guardar(mi, usuario:Usuario) -> None:
        userData = {"Nombre": usuario.getNombre(),
                    "Apellido": usuario.getApellido(),
                    "Edad": usuario.getEdad()}
        print(f"Guardando usuario de la bandeja:{mi.__bucket}:{userData}")
    
    def cerrar(mi) -> None:
        print("Cerrando conexión AWS S3")