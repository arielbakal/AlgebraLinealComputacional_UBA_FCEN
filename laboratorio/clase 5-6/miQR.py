
"""
Algebra Lineal Computacional - QR
"""

import numpy as np


def householder(x):
    
    #verifico que no sea un vector nulo (ie, su norma no es 0)
    assert np.linalg.norm(x, np.inf)>0, 'vector nulo!'
    
    
    # copio y transformo a un vector columna
    v = x.copy().reshape(-1,1)
    
    #  ***** COMPLETAR DESDE AQUI ******

    #  ***** COMPLETAR HASTA AQUI ******

    return v



def descomp_qr(A):
    
    m,n = A.shape
    assert m==n, 'las matriz debe ser cuadrada!'
    
    # R comienza siendo la matriz A y la usamos para ir triangulando
    R = A.copy()
    
    # Qt comienza siendo la indentidad y vamos acumulando el producto de las H
    Qt = np.identity(n)

    for j in range(0, n):
        
        
        # columna j-esima a triangular (considero elementos desde la diagonal)
        col_j = R[j:, j]

        #   Calcular el vector v que define la matriz de Householder.
        # v es un vector columna normalizado que servirá para construir H = I-2*v*v.T
        # v es de tamaño n-j
        v = householder(col_j)
        
        # H = I
        H = np.identity(n)
        
        # solo para las posiciones (j,j) en adelante (sin considerar filas
        #  o columnas anteriores a j-1): 
        # H = I - 2 * v * v.T    para la submatriz H[j:n,j:n]
        H[j:, j:] -= 2 * v * v.T
        
        # Verificamos que H es ortogonal.
        assert np.allclose(H.T @ H, np.identity(n)), 'H no es ortogonal!'
        
        # triangulamos la columna j-esima de R (que comienza siendo la matriz A)
        R = H @ R
        
        # Acumulamos en Qt el producto de las H's
        Qt = H @ Qt


    assert np.allclose( A, Qt.T @ R ), 'A no es igual a QR !'
    return Qt.T, R


n = 4

A = np.random.rand(n, n)

# QR de Numpy
q, r = np.linalg.qr(A)

# mi QR
Q, R = descomp_qr(A)


with np.printoptions(linewidth=9999, precision=20, suppress=True):
    print("**** mi Q")
    print(Q)
    print("**** Q de Numpy np.linalg.qr")
    print(q)
    print()
    
    print("**** mi R")
    print(R)
    print("**** R de Numpy np.linalg.qr")
    print(r)