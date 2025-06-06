import numpy as np
# Angel Vences Adame
## 9 Método de Newton
#a) f(x) = e^x + 2^(-x) + 2cos(x) - 6 = 0 para 1<= x <= 2
#asi f´(x) = e^x - 2^(-x)ln(2) - 2sin(x)
tol= 1e-6
n = 100 #numero de iteraciones maximas


def f(x):
    return np.exp(x) + 2**(-x) + 2*np.cos(x) - 6
def df(x):
    return np.exp(x) - 2**(-x)*np.log(2) - 2*np.sin(x)

x_0 = 1.5 #Punto medio de [1,2]
for i in range(n):
    x_i = x_0 - f(x_0) / df(x_0)  
    if abs(f(x_i)) < 1e-6:
        print("a) La raiz es:", x_i)
        break
    x_0 = x_i

#Generalizando...    
def newton(x_0,f,df,tol,n):
    for i in range(n):
        x_i = x_0 - f(x_0) / df(x_0)  
        if abs(f(x_i)) < tol:
            return x_i
        x_0 = x_i
    return None


#analogamente 
#b) f(x) = 2xcos(2x) - (x-2)^2 = 0 para 2 <= x <= 3 y 3 <= x <= 4
# entonces f´(x) = 2cos(2x) - 4xsin(2x) - 2(x-2)
x_0 = 2.5
def f2(x):
    return 2*x*np.cos(2*x) - (x - 2)**2
def df2(x):
    return 2*np.cos(2*x) - 4*x*np.sin(2*x) - 2*(x - 2)
print(f'b1) la primera raiz es {newton(x_0,f2,df2,tol,n)}')
x_0 = 3.5
print(f'b2) la segunda raiz es {newton(x_0,f2,df2,tol,n)}')

#c) f(x) = e^x - 3x^2 = 0 para 0 <= x <= 1 y 3 <= x <= 4
# entonces f´(x) = e^x - 6x
x_0 = 0.5 #inicial de la primera raiz
def f3(x):
    return np.exp(x) - 3*x**2
def df3(x):
    return np.exp(x) - 6*x

print(f'c1) la primera raiz es {newton(x_0,f3,df3,tol,n)}')
x_0 = 3.5 #inicial de la segunda raiz
print(f'c2) la segunda raiz es {newton(x_0,f3,df3,tol,n)}')
