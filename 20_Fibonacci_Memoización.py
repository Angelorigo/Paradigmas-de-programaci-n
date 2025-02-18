#  POR CORREGIR
#================================
#  Álvarez Servín Ángel Rodrigo
#================================
#  Paradigmas de Programación
#  Matemática Algorítmica
#  ESFM IPN  Noviembre 2024
#================================

#==============================
#  Recursividad y Memoización
#=============================

#====================================
#  Herramientas para la memoización
#====================================

from functools import lru_cache

def fibonacci_lento(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n>2:
        return fibonacci_lento(n-1)+fibonacci_lento(n-2)
    
for i in range (1, 10):
    print(str(i) + ":", fibonacci_lento(i))
    
    
#=========================================================
#  Optimización 1: Uso de conjuntos para guardar valores
#=========================================================

#===========================
#  Conjunto de fibonacci's
#===========================

fibonaccis = {}
def fibonacci(n):
    
    #==========================================
    #  Revisa si ya existe y regresa el valor
    #==========================================
    
    if n in fibonaccis[n]:
        return fibonaccis[n]
    
    if n == 1:
        valor = 1
    elif n ==2:
        valor = 1
    elif n>2:
        valor = fibonacci(n-1) + fibonacci(n-2)
    
    #============
    #  Guárdalo
    #============
    
    fibonaccis[n] = valor
    return valor

for i in range(1, 10):
    print(str(i) + ":", fibonacci(i))


#=======================================================
#  Uso de decoradores para memoización
#  "maxsize" es cuantos anteriores quieres que guarde
#=======================================================

@lru_cache(maxsize = 3)
def nfibonacci(n):
    if type(n) != int:
        raise TypeError("El valor de tu 'n' debe ser entero positivo")
    if n<1:
        raise ValueError("El valor de tu 'n' debe ser entero positivo")
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n>2:
        return nfibonacci(n-1) + nfibonacci(n-2)
    
for i in range(1, 10):
    print(str(i) + ":", nfibonacci(i))
    






















