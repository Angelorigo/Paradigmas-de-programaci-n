#================================
#  Álvarez Servín Ángel Rodrigoooooooo
#================================
#  Paradigmas de Programación
#  Matemática Algorítmica
#  ESFM IPN    Noviembre 2024
#================================

#============================================
#  Uso de reducciones (colapsar resultados)
#============================================

#===================================================
#  Multiplicación de todos los números en la lista
#===================================================

from functools import reduce
bigdata = [2,3,5,7,11,13,17,19,23,29]


#===============
#  Función x*y
#===============

multiplicar = lambda x,y: x*y
suma = lambda x,y: x+y
print(reduce(multiplicar, bigdata))
print(reduce(suma, bigdata))

#=============================================================
#  Reduce le aplica la función por partes a los resultados y
#  el siguiente elemento comenzando con los dos primeros
#  elementos.
#=============================================================
