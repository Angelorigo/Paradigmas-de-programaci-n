#================================
#  Álvarez Servín Ángel Rodrigo
#================================
#  Matemática Algorítmica
#  ESFM IPN 
#  Septiembre 2024
#================================

#=======================================================
#  Input permite obtener datos del usuario en prompter
#=======================================================

nombre = input("Dame tu nombre:  ")
print("Hola cómo estás ", nombre)

#==========================================
#  Los enteros son de precisión ilimitada
#==========================================

y = 50000000000000000000000000000000000
print(y)

#================================================================
#  Se pueden delimitar números con guión bajo, pero no con coma
#================================================================

y = 5_000_000
print(y)

#======================================================
#  La función int() cambia strings y floats a enteros
#======================================================

numero = int(input("Dame tu edad:  "))
type(numero)

#=====================================================
#  La notación científica de flotantes utiliza e o E
#=====================================================
#  1.2 x 10 a la (-9)
#======================

y = 1.2E-09
print(y)

#===========================================================
#  La función float() convierte strings y enteros a floats
#===========================================================

y = float("14.3")
print(y)

#======================================================
#  Los complejos se escriben con la raíz de menos uno 
#  j siempre con un número como prefijo
#  No acepta la j suelta
#======================================================

z = 1+1j

#  suma +
#  resta

