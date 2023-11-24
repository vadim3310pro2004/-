import numpy as np 
import matplotlib.pyplot as plt 
from scipy.interpolate import lagrange #імпортуємо функцію lagrange з бібліотеки scipy 


x = np.array([-3., -1., 1., 2.], dtype=float) 
y = np.array([3., 3., -13., -12.], dtype=float) 
points = (-4, -2, -1.5, 0.5) # точки, в яких потрібно обчислити значення 

 
def lagrange_interpolation(x, y, x_test): 
    n = len(x) 
    p = np.zeros(n) # масив для зберігання значень багаточленів L_i 

    for i in range(n): 
        p_i = 1 

        for j in range(n): 
            if i != j: 
                p_i *= (x_test - x[j])/(x[i] - x[j]) 

        p[i] = p_i 

    return np.dot(y, p) # повертаємо значення багаточлена у точці x_test 
 
# обчислюємо інтерполяційні багаточлени та їх значення в заданих точках 
for point in points:
    f_interp = lagrange_interpolation(x, y, point) 
    print(f"Значення функції у точці {point} = {f_interp}") 

# малюємо графіки 
xnew = np.linspace(np.min(x), np.max(x), 100) #точки, за якими будуємо графік 
ynew = [lagrange_interpolation(x, y, i) for i in xnew] 

plt.plot(x, y, 'o', xnew, ynew) #будуємо графік функції Лагранжа 
plt.title('Lagrange Polynomial_1') 
plt.grid(True) 
plt.show()

#Перевірка  
f = lagrange(x, y) 
fig = plt.figure(figsize = (7, 5)) 
plt.plot(xnew, f(xnew), 'b', x, y, 'ro') 
plt.title('Lagrange Polynomial_2') 
plt.grid() 
plt.xlabel('x') 
plt.ylabel('y') 
plt.show() 