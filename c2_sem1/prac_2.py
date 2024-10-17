import sympy as sp
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize

print("1: ")
x0 = 4
x = sp.symbols('x')
f = sp.sqrt(2 * x**3)
f_derivative = sp.diff(f, x)
f_derivative2 = sp.diff(f_derivative, x) 
print("Первая производная", f_derivative.subs(x, x0).evalf())
print("Вторая производная", f_derivative2.subs(x, x0).evalf())

print("2: ")
x = sp.symbols('x')
f = sp.sqrt(2 * x**3)
print("Первая производная", f_derivative)
print("Вторая производная", f_derivative2)

print("3: ")
def f3(x): 
    return np.sqrt(2 * x**3)
a = 2
b = 4 
print("Значение итнегралла на отрезке",quad(f3, a, b))

print("4: ")
integral = sp.integrate(f)
print(integral)

print("5: ")
def objective_function(v):
    x, y, z = v
    return (x - 1)**2 + (y - 3)**2 + (z - 4)**2
initial_guess = [0, 0, 0]
def constraint(v):
    x, y, z = v
    return -2 * x + y - z - 8 
constraints = ({'type': 'ineq', 'fun': constraint})
result = minimize(objective_function, initial_guess, constraints=constraints)
print(f"Оптимальное значение функции: {result.fun:.6f}")
print(f"Оптимальные значения переменных: x = {result.x[0]:.4f}, y = {result.x[1]:.4f}, z = {result.x[2]:.4f}")