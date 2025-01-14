#================================
#  Álvarez Servín Ángel Rodrigo
#================================
#  Paradigmas de Programación
#  Matemática Algorítmica
#  ESFM IPN   ENERO 2025
#================================

from mpi4py import MPI
import numpy


#=====================================================
#  Enviar objeto mensaje con comunicación bloqueada
#  (Cada proceso espera a que le reciban un mensaje)
#=====================================================

class Mensaje:
    def __init__(self, rank):
        #  ITERADOR
        self.x = range(rank*10)
        #  STRING 
        self.p = "Vengo del proceso "+str(rank)
        

#======================
#  Programa principal
#======================

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()
    s = Mensaje(rank)
    
    #  QUE TE MANDE EL ANTERIOR Y SI ES CERO QUE SEA EL ÚLTIMO
    fuente = rank-1 if rank!=0 else size-1
    
    #  MÁNDALO AL SIGUIENTE Y SI ERES EL ÚLTIMO MÁNDALO AL PRIMERO
    destino = rank+1 if rank!=size-1 else 0
    
    #============================================================
    #  send y recv son operaciones bloqueadas y gene0ran que el
    #  código se atore esperando que alguien reciba un mensaje.
    #  Esto se resuelve enviando con los pares y recibiendo con
    #  los impares.
    #============================================================
    
    # SI SOY PAR
    if rank%2==0:
        #  ENVIAR MENSAJE "S" AL DESTINO
        comm.send(s, dest = destino)
        
        #  RECIBIR DE SOURCE Y LO PONE EN "m"
        m = comm.recv(source = fuente)
    
    #  SI NO SOY PAR
    else:
        #  RECIBIR PRIMERO Y MANDAR MENSAJE DESPUÉS
        m = comm.recv(source = fuente)
        comm.send(s, dest = destino)
    
    print("Soy el proceso ", rank, ", el resultado es: ", len(m.x), ",", m.p)
    
    
    #==================================================================
    #  Para una comunicación más rápida se utilizan arreglos de numpy
    #  (send y recv van con mayúscula y cambian un poco)
    #  Se indica el tipo de datos explícitamente
    #==================================================================
    #  EJEMPLO 1 USANDO ENTEROS
    #==================================================================
    
    if rank == 0:
        #  ARREGLO DE ENTEROS DEL 1 AL 9
        data = numpy.arange(10, dtype='i')
        
        #  ENVÍO BLOQUEANTE ESPECÍFICANDO EL TIPO DE DATO
        comm.Send([data, MPI.INT], dest=1, tag=77)
        
    elif rank == 1:
        data = numpy.empty(10, dtype='i')
        comm.Recv([data, MPI.INT], source=0, tag=77)
        print(data)
        
    #============================================================
    #  También se puede sin decir el tipo de dato pero deben
    #  coincidir el tipo de arreglos a los extremos del mensaje
    #============================================================
    #  EJEMPLO 2 USANDO FLOTANTES
    #============================================================
    
    if rank == 0:
        data = numpy.arange(10, dtype=numpy.float64)
        comm.Send(data, dest=1, tag=13)
    
    elif rank == 1:
        data = numpy.empty(10, dtype=numpy.float64)
        comm.Recv(data, source=0, tag=13)
        print(data)
