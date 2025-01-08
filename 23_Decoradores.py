#================================
#  Álvarez Servín Ángel Rodrigo
#================================
#  Paradigmas de Programación
#  Matemática Algorítmica
#  ESFM IPN  Noviembre 2024
#================================

#====================================
#  Función que regresa otra función
#====================================

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper


#==================
#  Función Saludo
#==================

def say_hi():
    return "Hello There"


#============================
#  Generar y correr función
#============================

decorate = uppercase_decorator(say_hi)
print(decorate())


#===========================
#  Utilizar como decorador
#===========================

@uppercase_decorator
def say_hi():
    return "Hello there"


#=======================================
#  Correr función pasada por decorador
#=======================================

print(say_hi())