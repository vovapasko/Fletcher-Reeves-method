import math
import numpy
from tools import *
from function import *

epsilon = 0.01
epsilon_dich = 0.001
s0 = -(count_grad(x0, x, y))
s = [normalize(s0)]
x_values = [x0]
i = 0
fun_values = []


def get_gamma():
    b = (norm(count_grad(x_values[i + 1], x, y))) ** 2
    c = (norm(count_grad(x_values[i], x, y))) ** 2
    gamma = b / c
    return gamma

while True:
    print("i = ", i)
    print("(x, y) = ", x_values[i])
    fun_values.append(f(x_values[i]))
    print("f(x, y) =", fun_values[i])
    final_res = norm(count_grad(x_values[i], x, y))
    if final_res <= epsilon:
        print("Search is finished")
        break
    sven_interval = sven(x_values[i], s[i])
    point = dichotomy(x_values[i], sven_interval, s[i], epsilon)
    llambda = point['lambda']
    new_x = x_values[i] + llambda * s[i]
    x_values.append(new_x)

    grad = -count_grad(x_values[i + 1], x, y)
    gamma = get_gamma()
    s_gamma_product = s[i] * gamma
    new_s = grad + s_gamma_product

    new_s1 = normalize(new_s)
    s.append(new_s1)
    i += 1
    print("-------------------")

print("(x, y) = ", x_values[-1])
print("f(x, y) =", f(x_values[-1]))
