#Creacion pregunta numero 1
import scipy as sp 
import matplotlib.pyplot as plt 

def f(x):
    y=1/(1+25*x**2)
    return y

n=1 #Cantidad de puntos que utilizaremos
x_pts=np.linspace(-1,1,n) #Puntos equiespaciados en el intervalo [-1,1]
y_pts=f(x_pts) #Valores de la funcion evaluados en los puntos x_pts

#Interpolacion de Lagrange

def p_j(x,j): #Polinomio correspondiente a la posicion j que corresponda
    p=1
    for k in range(0,len(x)):
        if k!=j:
            p=p*((x-x[k])/(x[j]-x[k]))
    return p

def P(x): #Polinomio de interpolacion Lagrange
    S=0
    for j in range(0, len(x)):
        S=S+p_j(x,j)*y_pts[j]
    return S

#Grafico a 5 puuntos del polinomio de interpolacion
plt.plot(x_pts, y_pts, 'o', ms=5, label="Puntos (x,y)")
plt.plot(x_pts,P(x_pts), color="g", label="P(x) a 5 puntos")
plt.xlabel("X")  
plt.ylabel("Y") 
plt.legend(loc="upper right")
plt.show()



#Aproximacion de empalme("spline") cubico

from scipy.interpolate import InterpolatedUnivariateSpline as ius


plt.clf()
spl = ius(x_pts, y_pts)
plt.plot(x_pts, y_pts, 'o', ms=5, label="Puntos (x,y)")
xs = np.linspace(-1, 1, n)
plt.plot(xs, spl(xs), 'g', lw=1, alpha=0.7, label="Spline a 5 puntos")
plt.xlim(-1.1,1.1)
plt.ylim(0,1.1)
plt.xlabel("X")  
plt.ylabel("Y") 
plt.legend(loc="upper right")
plt.show()

#Comparacion de metodos

a=f(x_pts)
b=P(x_pts)
c=spl(xs)
i= b-a
j= c-a
plt.plot(x_pts,i, color="g", label="Polinomio")
plt.plot(x_pts,j, color="b", label="Spline")
plt.xlabel("X")  
plt.ylabel("Y") 
plt.legend(loc="upper right")