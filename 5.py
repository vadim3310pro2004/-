
import matplotlib.pyplot as plt 
from scipy import optimize 
from math import cos, sin 
import numpy as np 

# область значень для x та y 
x_min, x_max = -1, 1 
y_min, y_max = -4, 1 
step = 0.01 

# створюємо масиви значень x та y 
x, y = np.meshgrid(np.arange(x_min, x_max, step), 
                   np.arange(y_min, y_max, step)) 
# рівняння системи 
eq1 = 2*x - np.cos(y+1) 
eq2 = y + np.sin(x) + 0.4 
# створюємо графік 
fig, ax = plt.subplots(figsize=(10, 10)) 
# додаємо графік першого рівняння 
ax.contour(x, y, eq1, levels=[0], colors='red') 
# додаємо графік другого рівняння 
ax.contour(x, y, eq2, levels=[0], colors='blue') 
# налаштування графіка 
ax.set_xlim([x_min, x_max]) 
ax.set_ylim([y_min, y_max]) 
ax.set_xlabel('x') 
ax.set_ylabel('y') 
ax.set_title('Графік системи рівнянь') 
plt.grid(True) 
# показуємо графік 
plt.show() 
# далі розв'язок системи рівнянь методом простої ітерації 

x0, y0 = 0.3, -0.7 
delta = 0.1 

# задаємо функції 
def f1(y): 
    return cos(y+1) / 2 


def f2 (x): 
    return -0.4 - sin(x) 


def iter (x, y, e): 
    xn, yn = x, y 
    xn1, yn1 = f2(x), f1(y) 
    n = 1 

    while ((abs(xn1-xn) >= e) & (abs(yn1-yn) >= e)): 
        xn, yn = xn1, yn1 
        xn1, yn1 = f2(yn), f1(xn) 
        n += 1 

    print ('Simple iteration:') 
    print ('x=', xn, '\ny=', yn, '\nThe amount of iteration = ', n) 
 

iter(x0, y0, 0.0001) 


def f3(x): 
    return 3*x[0] - cos(x[1])  - 0.9, sin(x[0] - 0.6) - x[1] -1.6 

# перевірка розв'язку відповіді мають співпасти 
s = optimize.root(f3, [0., 0.], method = 'hybr') 
print ('Chek', s.x) 