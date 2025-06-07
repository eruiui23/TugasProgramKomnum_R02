import numpy as np
import sympy as sp

def Et (x_seb, x_n):
    return abs((x_seb-x_n)/x_seb)

def Ea (x_n, x0):
    return abs((x_n - x0)/x_n) if x_n != 0 else float('inf')

def NewtonRaphsonModif(f, x0, x_seb, max_iter=3):
    x = sp.symbols('x')
    f_turunan1 = f.diff(x)
    f_turunan2 = f_turunan1.diff(x)
    x_n = x0

    for i in range (max_iter):
        f_value = f.subs(x, x_n)
        f_turunan1_value = f_turunan1.subs(x,x_n)
        f_turunan2_value = f_turunan2.subs(x,x_n)

        # if (f_turunan1_value or f_turunan2_value == 0)
        #     raise ValueError("Turunannya 0, tidak ditemukan solusi")

        x_n = round(x_n - ((f_value * f_turunan1_value)/((f_turunan1_value)**2 - f_value*f_turunan2_value)),2)
        Et_value = round(Et(x_seb, x_n), 2)
        Ea_value = round(Ea(x_n, x0), 2)
        x0 = x_n
        print(f"Iteration {i+1}: x_n = {x_n}, Et = {Et_value}, Ea = {Ea_value}")
        # print(f"Iteration {i+1}: x_n = {x_n:.2f}, Et = {Et_value:.2f} %, Ea = {Ea_value:.2f} %")


f = input("Masukan fungsi f(x): ")
f = sp.sympify(f)
x0 = float(input("Masukan x0: "))
x_seb = float(input("masukan nilai sebenarnya: "))
NewtonRaphsonModif(f,x0, x_seb)

# contoh
# f(x) = 2*x**3-2*x**2-42*x+90
# x0 = 2
# x_seb = 3

# contoh 2
# 12*x**3-30*x**2-84*x+48
# -1
# -2
