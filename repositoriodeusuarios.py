from aplicacion.modelos.usuario import Usuario

#================================
#  Este objeto es una interfase
#================================

class RepositorioDeUsuarios:
    def abrir(mi) -> None:
        pass
    def guardar(mi, usuario: Usuario) -> None:
        pass
    def cerrar (mi) -> None:
        pass