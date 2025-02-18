#================================
#  Álvarez Servín Ángel Rodrigo
#================================ 
#  Matemática Algorítmica
#  Paradigmas de Programación
#  ESFM IPN  Octubre 2024
#================================

#=================================
#  Importación de módulos
#  Contienen objetos y funciones
#=================================

import matplotlib.pyplot as grafica
import math


#=======================
#  Función Exponencial
#  Serie de Taylor 
#  Polinomio en orden
#=======================

def exponencial(n: int = 1500, x: float = 0.5): 
  factorial = 1.0
  exponencial_de_x = 1.0
  x_a_la_n = 1.0
  for i in range(1,n):
    x_a_la_n *= x
    factorial *= float(i)
    s = 1.0 / factorial
    exponencial_de_x += s*x_a_la_n
  return exponencial_de_x

def exponencial_pro(n: int = 1500, x: float = 0.5):
  flag = False
  if x<0:
    flag = True
    x = -x
  s = 1.0
  for i in range(n, 0, -1):
      s *= x / float(i)
      s += 1.0
  if flag == True:
    s= 1 / s
  return s

m = 400
serie = 250
error1 = []
error2 = []
x0 = 0.0
b = list(range(m))
x = [x0+n*0.1 for n in b]  #  Multiplicar una lista por un número

for i in range(m):
   y = x0+0.1*i
   error1.append(exponencial(serie, y)-math.exp(y))
   error2.append(exponencial_pro(serie, y)-math.exp(y))

grafica.subplot(211)
grafica.plot(x, error1)
grafica.subplot(212)
grafica.plot(x, error2)
grafica.show()
