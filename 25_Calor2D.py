#  PIDE NUMBA
#================================
#  Álvarez Servín Ángel Rodrigo
#================================
#  Paradigmas de Programación
#  Matemática Algorítmica
#  ESFM IPN  Noviembre 2024
#================================

#==================================================
#  Importar numpy, matplotlib, mpl_toolkits, time
#==================================================

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import time


#====================================
#  Parámetros que se puedan cambiar
#====================================

#  Número de celdas
n = np.array([1, 1])

#  Tamaño del dominio (menor que uno)
L = np.array([1.0, 1.0])

#  Constante de difusión
k = 0.2

#  Pasos de tiempo
pasos = 100


#================================================
#  Parámetros secundarios (no se deben cambiar)
#================================================

#  Tamaños de las celdas
dx = L/n
udx2 = 1.0/(dx*dx)

#  Paso de tiempo
dt = 0.25*(min(dx[0], dx[1])**2)/k
print("dt = ", dt)

#  Total de celdas
nt = n[0]*n[1]
print("Celdas = ", nt)


#======================
#  Arreglos iniciales
#======================

#  Llenar la solución con ceros
u = np.zeros(nt, dtype = np.float64)   #  Arreglo de lectura
un = np.zeros(nt, dtype = np.float64)  #  Arreglo de escritura


#==========================================================
#  Evolución temporal de la ecuación diferencial parcial
#  u_t = k*laplaciano(u)  (ecuación de difusión de calor)
#==========================================================

def evolucion(u, n, udx2, dt, i, k):
    jp1 = i + n[0]
    jm1 = i - n[0]
    laplaciano = (u[i-1] - 2.0*u[i] + u[i+1])*udx2[0] + (u[jm1] - 2.0*u[i] + u[jp1])*udx2[1]
    unueva = u[i] + dt*k*laplaciano
    return unueva


#==================================================================
#  Loop sobre toda la malla para avanzar la ecuación en el tiempo
#  No contiene la frontera (u = 0 en toda la orilla del dominio)
#==================================================================

def solucion(u, un, udx2, dt, n, k):
    for jj in range (1, n[1] - 1):
        for ii in range (1, n[0] - 1):
            i = ii + n[0]*jj
            
            #  Avanzar la ecuación en un punto
            unueva = evolucion(u, n, udx2, dt, i, k)
            
            #  En medio de la malla poner temperatura fija 1
            if i == int(nt/2) + int(n[0]/2):
                unueva = 1.0
            un[i] = unueva
            

#======================
#  PROGRAMA PRINCIPAL
#======================

solucion(u, n, udx2, dt, n, k)
start = time.time()

#  Pasos de tiempo
for t in range(1, pasos + 1):
    
    #  Avanzar ecuación en toda la malla
    solucion(u, n, udx2, dt, n, k)
    
    #  Copiar arreglo nuevo al viejo
    u = un
    
    #  Avisar en pantalla el paso en el que va
    if t%10==0: print("Iteración = ", t)
    
end = time.time()
print("Tardó: ", end-start, "s")


#==========================================
#  Gráfico de la solución al tiempo final
#==========================================

u = np.reshape(u, (n[0], n[1]))
x,y = np.meshgrid(np.arange(0, L[0], dx[0]), np.arange(0, L[1], dx[1]))
ax = plt.axes(projection = "3d")
ax.plot_surface(x, y, u, cmap = cm.hsv)
plt.show()
