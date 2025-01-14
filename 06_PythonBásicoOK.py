#================================
#  Ángel Rodrigo Álvarez Servín
#================================
#  Matemática Algorítmica
#  Paradigmas de Programación
#  ESFM IPN     Octubre 2024
#================================

#======================
#  Mi primera función
#======================

def saludo():
    #====================================== 
    #  Documentación rápida de la función
    #======================================
    """Esta función saluda"""
    print("Quiúboles, ¿cómo estás?")


#=========================
#  Llamado de la función
#=========================

saludo()


#================================
#  Se ejecuta pero no se asigna
#================================

salida = saludo()


#====================
#  Esto no funciona
#====================

#print(salida)


#=========================
#  Mostrar documentación 
#=========================

#help(saludo)


#=========================
#  Función con argumento
#=========================

def salu2(nombre):
    """Esta función te saluda por tu nombre"""
    print("¡Qué onda ese ", nombre, "!")
salu2("Ángel")
salu2("Servín")


#===========================================
#  Ahorrar trabajo del intérprete
#  nombre:str la variable nombre es un str
#===========================================

def saludos(nombre:str):
    """Esta función te saluda por tu nombre estrictamente"""
    print("Qué onda ese ", nombre, "!")
saludos("Servín")
a = 10
print(type(a))
saludos(a)


#=================================
#  Función con muchos argumentos
#=================================

def saludos_multiples(nombre1, nombre2, nombre3):
    """Esta función saluda a tres personas al mismo tiempo"""
    print("Hola ", nombre1, ",", nombre2, "y ", nombre3)
saludos_multiples("Ángel","Fernanda","Juan")


#==============================================
#  Función con cualquier número de argumentos
#==============================================

def muchos_saludos(*nombres):
    """Esta función saluda a todos los que quieras"""
    i = 0
    #===================================
    #  end= es para ponerlo de corrido
    #===================================

    print("Hola ", end=" ")
    while len(nombres) > i:
      #  Último nombre
      if (i==len(nombres) - 1):
        print(nombres[i])
      else:
        #  Cualquier otro nombre
        print(nombres[i], end= " ,")
      i+=1

muchos_saludos("Nicole","Enrique", "Alejandro", "Iván", "Zaid", "Joel", "Servín")

def greet(firstname, lastname):
    print ("Hello", firstname, " ", lastname)


#================================================
#  Llamar la función con argumentos en desorden
#================================================

greet(lastname= "Servín", firstname= "Ángel")


#========================================
#  Función con argumentos escondidos **
#========================================

def greet(**person):
    #======================================================
    #  Persona tiene características firstname y lastname
    #======================================================
    print("Hallo ", person["firstname"], " ", person["lastname"])

greet(firstname= "Steve", lastname= "Jobs")
greet(lastname= "Jobs", firstname= "Steve")
greet(firstname= "Bill", lastname= "Gates", age= 55) #  Se pueden pasar más parámetros de los necesarios


#===================================
#  Función con valores por defecto
#===================================

def greet(name= "Stanger"):
    print("Hellow ", name)

greet()  #  Utiliza el valor dado de antemano
greet("Steeve")


#=========================
#  Función con resultado
#=========================

def suma (a, b):
    return a + b


#================================================
#  Programación funcional
#  Se pueden usar funciones dentro de funciones
#================================================

total= suma(5, suma(10, 20))
print(total)


#===================================================
#  Cálculo de lambda
#  Nombre de la función = lambda variable: función
#===================================================

x_al_cuadrado = lambda x : x*x
a1 = x_al_cuadrado(5)
print(a1)


#==============================
#  Lambda de varias variables
#==============================

suma = lambda x1, x2, x3: x1+x2+x3
print(suma(99, 98, 97))

sumas = lambda *x: x[0]+x[1]+x[2]+x[3]
print(sumas(100, 200, 300, 400))


#===========================================
#  Uso de una función anónima
#  El argumento va afuera entre paréntesis
#===========================================

print((lambda x: x*x)(6))  #  Función anónima


#===============================
#  Función con variable global
#  EVITE EL EXCESO!!!
#===============================

name = "Steveeeee"
def greet():
    global name  #  Para utilizar una variable global (que viene de fuera del bloque)
    name = "Billl"
    print("Holi ", name)

greet()
