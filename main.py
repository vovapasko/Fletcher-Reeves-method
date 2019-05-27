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


def get_point():
    sven_interval = sven(x_values[i], s[i])
    point = dichotomy(x_values[i], sven_interval, s[i], epsilon_dich)
    return point


def fx_criterion(par_epsilon):
    delta_x = norm(x_values[i] - x_values[i - 1]) / norm(x_values[i - 1])
    delta_f = math.fabs((f(x_values[i]) - f(x_values[i - 1])) / f(x_values[i - 1]))
    if delta_x <= par_epsilon and delta_f <= epsilon:
        return True
    return False


def norm_grad_criterion(par_epsilon):
    norm_gradient = norm(count_grad(x_values[i], x, y))
    if norm_gradient <= par_epsilon:
        return True
    return False


while True:
    print("i = ", i)
    print("(x, y) = ", x_values[i])
    fun_values.append(f(x_values[i]))
    print("f(x, y) =", fun_values[i])
    point = get_point()
    llambda = point['lambda']
    new_x = x_values[i] + llambda * s[i]
    x_values.append(new_x)

    minus_grad = -count_grad(x_values[i + 1], x, y)
    gamma = get_gamma()
    s_gamma_product = s[i] * gamma
    new_s = minus_grad + s_gamma_product

    new_s1 = normalize(new_s)
    s.append(new_s1)
    if fx_criterion(epsilon):
        print("Search is finished")
        break

    i += 1
    print("-------------------")

print("(x, y) = ", x_values[-1])
print("f(x, y) =", f(x_values[-1]))
