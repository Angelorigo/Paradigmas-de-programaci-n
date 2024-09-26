#================================
#  Álvarez Servín Ángel Rodrigo
#================================
#  Paradígmas de programación 
#  Matemática Algorítmica
#  ESFM-IPN    Sept-2025
#================================

''' ESTE ES UN SUPERCOMENTARIO  
    DE INICIO A NUESTRO RESUMEN
'''
#=======================
#  Operaciones básicas
#=======================
print (2+3)
print (2*3)
print (2/3)
print (2**10)   #potencia
print (2**1.5)  #raíz cuadrada
print (10%2)
print (20%0.1)  #Exclusivo de python

#============================================
#  Para saber el tipo de objeto se usa type 
#============================================ 

t=0
print (type(t))   #entero
t=3.6
print (type(t))   #real (flotante)
t=True
print (type(t))   #booleano (bool)

#========================
#  Mensajes en pantalla 
#========================

print ("Este es un comando de python. ", "Este es otro encunciado. ",t)
print ('id:  ', 1)
print ('Nombres: ', 'Steve')
print ('Apellidos: ', 'Jobs')
print ("vamos a sumar esto " + " con esto otro")

#=================================================
#  Continuar una instrucción en varios renglones 
#=================================================

if 100 > 99 and \
    200 <= 300 and \
    True != False:
	print ('Hola a todos')

#=========================================
#  Comandos diferentes en la miama línea
#=========================================

print ("Hola "); print ("tu")     #Se considera mala práctica

#==================================================
#  Usando paréntesis redondos, cuadrados o llaves
#  se puede escribir en varios renglones
#==================================================

lista = [1, 2, 3, 4,
	5, 6, 7, 8,
	9, 10, 11,12]

matriz = [ [1,2,3,4], [5,6,7,8], [9, 10, 11, 12] ]

print (lista)
print (matriz)

#====================================================================
#  Identación estricta para procesos dependientes de : (dos puntos)
#====================================================================

if 10>5:
   print ("diez mayor que cinco")
   print ("otra identación")
for i in lista:
   print (i)
   print ("Ok")
if 10>5:
   print ("verdadero")
if 10<20:
   print ("verdadero")
elif 5>3: #comienza segundo condicional
   print ("esto no se imprimirá")
else:
   print ("aquí nunca llega")

#=============
#  Funciones
#=============
def saludar (nombre):
   print ("Hola ", nombre)
   print ("Bienvenido al tutorial de python")

saludar ("Servín") 
