import math
import numpy
from tools import *
from function import *

epsilon = 0.001
epsilon_dich = 0.0001
s0 = -(count_grad(x0))
s = [s0]
x_values = [x0]
i = 0
fun_values = [f(x0)]
min_vector_grad = []


def get_gamma():
    b = (norm(count_grad(x_values[i + 1]))) ** 2
    c = (norm(count_grad(x_values[i]))) ** 2
    gamma = b / c
    return gamma


def get_point():
    sven_interval = sven(x_values[i], s[i])
    if sven_interval == False:
        return False
    point = dichotomy(x_values[i], sven_interval, s[i], epsilon_dich)
    return point


def fx_criterion(par_epsilon):
    delta_x = norm(x_values[i] - x_values[i - 1]) / norm(x_values[i - 1])
    delta_f = math.fabs((f(x_values[i]) - f(x_values[i - 1])) / f(x_values[i - 1]))
    if delta_x <= par_epsilon and delta_f <= epsilon:
        return True
    return False


def norm_grad_criterion(par_epsilon):
    norm_gradient = norm(count_grad(x_values[i]))
    if norm_gradient <= par_epsilon:
        return True
    return False


while True:
    print("i = ", i)
    print("(x, y) = ", x_values[i])
    print("f(x, y) =", fun_values[i])
    point = get_point()
    if point == False:
        s[-1] = -count_grad(x_values[-1])
        continue
    llambda = point['lambda']
    new_x = x_values[i] + llambda * s[i]
    x_values.append(new_x)
    fun_values.append(f(x_values[i]))

    minus_grad = -count_grad(x_values[i + 1])
    min_vector_grad.append(minus_grad)
    gamma = get_gamma()
    s_gamma_product = s[i] * gamma
    new_s = minus_grad + s_gamma_product

    # new_s1 = normalize(new_s)
    s.append(new_s)
    if norm_grad_criterion(epsilon):
        print("Search is finished")
        break

    i += 1
    print("-------------------")

print("(x, y) = ", x_values[-1])
print("f(x, y) =", f(x_values[-1]))
draw_plot(x_values, real_min_point)
