#================================
#  Álvarez Servín Ángel Rodrigo
#================================
#  Paradigmas de Programación
#  Matemática Algorítmica
#  ESFM IPN  Octubre 2024
#================================

#=====================
#  Clase computadora
#=====================

class Computadora:
    marca: str = None
    capacidad: int = 0
    ram: int = 0

    #  CONSTRUCTOR
    def __init__(self, marca:str, capacidad:int, ram:int):
        print(f"Accediendo al constructor de la pc: {marca}")
        self.marca = marca
        self.capacidad = capacidad
        self.ram = ram

    def imprimirInfoPC(self):
        print(f"Esta es la computadora marca: {self.marca} con almacenamiento de {self.capacidad}GB y memoria de: {self.ram}GB")
    
    #  DESTRUCTOR
    def __del__(self):
        print(f"Se eliminó la computadora: {self.marca}")


#=================
#  Clase Persona
#=================

class Persona:
    nombres: str = None
    apellidos: str = None
    edad: int = 0
    direccion: str = None
    computadora: Computadora = None

    #  CONSTRUCTOR DE PERSONA
    def __init__(self, nombres:str, apellidos:str, edad:int, direccion:str, marca:str, capacidad:int, ram:int):
        self.nombres = nombres
        self.apellidos = apellidos
        self.edad = edad
        self.direccion = direccion
        self.Computadora = Computadora(marca, capacidad, ram)
        print(f"--- Accedimos al constructor de persona: {nombres} {apellidos}")
    def imprimirInfo(self) -> None:
        print(f"--- Mi nombre es {self.nombres} {self.apellidos}, tengo {self.edad} años de edad, vivo en {self.direccion}")
        self.Computadora.imprimirInfoPC()

    #  DESTRUCTOR 
    def __del__(self):
        print(f"--- Eliminamos a la persona: {self.nombres} {self.apellidos}")


#============================
#  Función 1 es el programa
#============================

def funcion1():
    persona = Persona("Carlos", "Pérez", 40, "Xochimilco", "Lenovo", 700, 8)
    print("\n")
    persona.imprimirInfo()
    print("\n")    
    persona2 = Persona("Maggie", "Carrillo", 35, "Jalapa","IBM", 200, 4)
    persona2.imprimirInfo()
    print("\n")


#======================
#  Llamar a función 1
#======================

funcion1()
