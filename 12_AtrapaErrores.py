#  POR CORREGIR
#================================
#  Álvarez Servín Ángel Rodrigo
#================================
#  Matemática Algorítmica
#  Paradigmas de Programación
#  ESFM IPN   Noviembre 2024
#================================

#=====================================================
#  La clase ClienteBancario está en el subdirectorio
#  aplicacion/banco/
#=====================================================

from aplicacion.banco.cliente_bancario import ClienteBancario


#==============================================
#  try: intenta (correr las instrucciones)
#  except: atrapar el error en una variable e
#  e se puede convertir en string
#==============================================

#============================================
#  Error por sacar más dinero del que tiene
#============================================

try:
    cliente = ClienteBancario("Jaime Andrade", "Hernández Sánchez", 28, 0.0)
    cliente.guardarDinero(300)
    print(cliente.imprimirInfo())
    cliente.retirarDinero(400)
    print(cliente.imprimirInfo())
    

#===============================================
#  Exception es el objeto más general de error
#===============================================

except Exception as e:
    print("Error: " + str(e))
    

#======================================
#  Error por usar un atributo privado
#======================================

try:
    print(cliente.__nombres)
except Exception as ex:
    print("Error: " + str(ex))


#==================
#  Forma correcta
#==================

print(cliente.nombres)













































































