from matplotlib import pyplot as plt
import numpy as np
import sys

def dibujarVector(ax, orig, fin, color, tex=None):
    # orig y fin son dos vectores columna
    x = [orig[0], fin[0]]
    y = [orig[1], fin[1]]
    ax.plot(x,y,'-', color=color)
    if tex is not None:
        ax.text(fin[0]/2, fin[1]/2, tex)
    

def dibujarPuntos(ax, pts, color):
    pts = np.array(pts)
    ax.plot(pts[:,0], pts[:,1], '*', color=color)

def main(N):
        
    orig = np.array([[0],[0]])
    A = np.array([[1, 3], [4,2]]) / 4
    x = np.array([[1],[0]])
    Ax = np.matmul(A, x)
    
    fig, ax = plt.subplots()
    dibujarVector(ax,orig, x,'b')
    dibujarVector(ax,orig, Ax, 'g')
    
    ax.set(aspect='equal',xlim=[-2,2], ylim=[-2,2])
    
    # digujar el ciruclo unitario y la proyección de los puntos
    t = np.linspace(0, 2 * np.pi, N)
    
    xPts = []
    AxPts = []
    
    for k in range(N):
        fig, ax = plt.subplots()
        
        x = np.array([[np.cos(t[k])],[np.sin(t[k])]])
        ax.set_title(r'$x = (%1.3f, %1.3f)^t$' % (x[0], x[1]))
        
        Ax = A @ x
        xPts.append(x.squeeze()) # 2x1 vector
        AxPts.append(Ax.squeeze())
        
        dibujarVector(ax, orig, x, 'b', tex='x')
        dibujarVector(ax, orig, Ax, 'g', tex='Ax')
        
        dibujarPuntos(ax, xPts, 'b')
        dibujarPuntos(ax, AxPts, 'g')
    
        ax.set(aspect='equal',xlim=[-2,2], ylim=[-2,2])
        ax.plot()
        # descomentar si se ejecuta desde la linea de comandos, para
        # que el usuario vaya viendo las gráficas y tenga tiempo de 
        # evaluar los vectores
        # plt.waitforbuttonpress(timeout=-1)
        # plt.close()
        ################################################3

if __name__ == "__main__":
    N = 10 # define la granularidad en la cantidad de puntos graficados
    
    args = sys.argv[1:]
    if len(args) == 2 and args[0] == '--N':
        N = int(args[1]) 
    else:
        print('Carga de parametros incorrecta o incompleta.')
        print('Se utiliza --N X para indicar el valor de N.')
        print('utilizaremos el valor de N por default')
    main(N)
