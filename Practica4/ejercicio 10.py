#10 Calcular las raices usando metodo de la secante
#definimos la funcion secante
def secante(x_0, x_1, f, tol, n):
    for i in range(n):
        if abs(f(x_1)) < tol:
            return x_1
        x_i = x_1 - f(x_1) * (x_1 - x_0) / (f(x_1) - f(x_0))
        x_0, x_1 = x_1, x_i
    return None

#Asi
#a) f(x) = e^x + 2^(-x) + 2cos(x) - 6 = 0 para 1<= x <= 2
a_sec = secante(1.5, 1.6, f, tol, n)
print(f'La raiz por secante a) es {a_sec}')

#b) f(x) = 2xcos(2x) - (x-2)^2 = 0 para 2 <= x <= 3 y 3 <= x <= 4
b1_sec = secante(2.5, 2.6, f2, tol, n)
print(f'La primera raiz por secante b) es {b1_sec}')
b2_sec = secante(3.5, 3.6, f2, tol, n)
print(f'La segunda raiz por secante b) es {b2_sec}')
#c) f(x) = e^x - 3x^2 = 0 para 0 <= x <= 1 y 3 <= x <= 4
c1_sec = secante(0.5, 0.6, f3, tol, n)
print(f'La primera raiz por secante c) es {c1_sec}')
c2_sec = secante(3.5, 3.6, f3, tol, n)
print(f'La segunda raiz por secante c) es {c2_sec}')