#  CUDA
#================================
#  Ángel Rodrigo Álvarez Servín
#================================
#  Paradigmas de Programación
#  Matemática Algorítmica
#  ESFM IPN  Noviembre 2024
#================================

#===============================
#  Importar módulos necesarios
#===============================

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import time
from numba import jit
from numba import cuda
from numba import *


#=========================
#  Parámetros de entrada
#=========================

#  Número de celdas
n = np.array([512, 512], dtype = np.int64)

#  Tamaño del dominio (menor que uno)
L = np.array([1.0, 1.0], dtype = np.float64)

#  Constante de difusión
kd:float64 = 0.2

#  Pasos de tiempo
pasos:int = 100000


#==========================
#  Parámetros secundarios
#==========================

#  Tamaños de las celdas
dx = L/n
udx2 = 1.0/(dx*dx)

#  Pasos de tiempo
dt = 0.25*(min(dx[0], dx[1])**2)/kd
print("dt = ", dt)

#  Total de celdas
nt = n[0]*n[1]
print("Celdas = ", nt)


#====================================
#  Función sin intérprete de python
#====================================

@jit(nopython = True)
def evolucion(u, n_0, n_1, udx2_0, udx2_1, dt, kd, i):
    jp1 = i + n_0
    jm1 = i - n_0
    laplaciano = (u[i-1] - 2.0*u[i] + u[i+1])*udx2_0 + (u[jm1] - 2.0*u[i] + u[jp1])*udx2_1
    unueva = u[i] + dt*kd*laplaciano
    return unueva


#=======================
#  Función para el GPU
#=======================
 
evolucion_gpu = cuda.jit(device = True)(evolucion)


#===========================
#  Rutina de CUDA (nvidia)
#===========================

@cuda.jit
def solucion_kernel(u_d, un_d, udx2_0, udx2_1, dt, n_0, n_1, kd):
    ii, jj = cuda.grid(2)
    i = ii + n_0+jj
    if ii == 0 or jj == 0 or ii == n_0-1 or jj == n_1-1:
        unueva = 0.0
    else:
        unueva = evoluciongpu(u_d, n_0, n_1, udx2_0, udx2_1, dt, kd, i)
    if i == int((n_0*n_1)/2) + int(n_0/2):
        unueva = 1.0
    un_d[i] = unueva
    
blockdim = (32, 16)                                       #  Hilos por bloque
griddim = (int(n[0]/blockdim[0]), int(n[1]/blockdim[1]))  #  Bloques en el dominio


#======================
#  PROGRAMA PRINCIPAL
#======================

start = time.time()


#================================
#  Llenar la solución con ceros
#================================

u  = np.zeros(nt, dtype = np.float64)  #  Arreglo de lectura
un = np.zeros(nt, dtype = np.float64)  #  Arreglo de escritura


#=========================
#  Pasar arreglos al GPU
#=========================

u_d = cuda.to_device(u)
un_d = cuda.to_device(un)


#=========================
#  Integrar en el tiempo
#=========================
 
for t in range(1, pasos + 1):
    solucion_kernel[griddim, blockdim](u_d, un_d, udx2[0], udx2[1], dt, n[0], n[1], kd)
    
    #  Copiar arreglo dentro del GPU
    u_d = cuda.to.device(un_d)
    if t%100==0: print("Paso = ", t)


#========================
#  Pasar arreglo al CPU
#========================

u_d.copy_to_host(u)
end = time.time()
print("Tardó: ", end-start, "s")


#==================
#  Graficar en 3D
#==================

u = np.reshape(u, (n[0], n[1]))
x,y = np.meshgrid(nd.arange(0, L[0], dx[0]), np.arange(0, L[1], dx[1]))
ax = plt.axes(projection = "3d")
ax.plot_surface(x, y, u, cmap = cm.hsv)
plt.show()
