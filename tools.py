import math
import numpy as np
import sympy
from sympy import diff
from function import *
import matplotlib.pyplot as plt


def draw_plot(title_function,values, min_point):
    plt.title(title_function)
    plt.plot([x[0] for x in values], [x[1] for x in values], 'b')
    plt.plot(min_point[0], min_point[1], 'r-o')
    plt.show()


def count_grad(given_fun, point):
    diff_f_x = sympy.diff(given_fun, x)
    diff_f_y = sympy.diff(given_fun, y)
    f_x_point = diff_f_x.subs({x: point[0], y: point[1]})
    f_y_point = diff_f_y.subs({x: point[0], y: point[1]})
    return np.array([f_x_point, f_y_point])





def normalize(vector):
    a1 = norm(vector)
    res = vector / norm(vector)
    return vector / norm(vector)


def sven(par_function, x, s):
    llambda = get_lambda(x, s)
    x0_minus = get_x(x, s, -llambda)
    x0_plus = get_x(x, s, llambda)
    k = 1
    i = 0
    fc = 0
    x_values = []
    fminus = f(par_function, x0_minus)
    fc += 1
    fplus = f(par_function, x0_plus)
    fc += 1
    if fminus < fplus:
        return False
        # llambda = -llambda
        # x_values.append({'lambda': llambda, 'value': x0_minus})
    else:
        x_values.append({'lambda': llambda, 'value': x0_plus})
    while True:
        new_lambda = x_values[i]['lambda'] + (2 ** k) * llambda
        xk_next = get_x(x, s, new_lambda)
        fk = f(par_function, x_values[i]['value'])
        fc += 1
        fk_next = f(par_function, xk_next)
        fc += 1
        x_values.append({'lambda': new_lambda, 'value': xk_next})
        if fk_next > fk and len(x_values) == 2:
            a = x_values[0]
            b = x_values[1]
            middle_lambda = (b['lambda'] + a['lambda']) / 2
            middle_value = get_x(x, middle_lambda, s)
            print("Count sven interval function in - ", fc)
            return a, {'lambda': middle_lambda, 'value': middle_value}, b
        if fk_next > fk:
            a = x_values[-3]
            x_m = x_values[-2]
            b = x_values[-1]
            middle_lambda = (b['lambda'] + x_m['lambda']) / 2
            middle_value = get_x(x, middle_lambda, s)
            print("Count sven interval function in - ", fc)
            return a, x_m, {'lambda': middle_lambda, 'value': middle_value}

        else:
            k += 1
            i += 1


def dichotomy(par_function, point, interval, s, epsilon):
    a = interval[0]
    x_m = interval[1]
    b = interval[2]
    k = 1
    fc = 0
    while True:
        a_lambda = a['lambda']
        b_lambda = b['lambda']
        L = (b_lambda - a_lambda)
        if math.fabs(L) < epsilon:
            print("dichotomy count in - ", fc)
            return x_m
        new_x1_lambda = a_lambda + L / 4
        new_x2_lambda = b_lambda - L / 4
        new_x1_value = get_x(point, s, new_x1_lambda)
        new_x2_value = get_x(point, s, new_x2_lambda)
        f_x1 = f(par_function, new_x1_value)
        f_xm = f(par_function, x_m['value'])
        f_x2 = f(par_function, new_x2_value)
        fc += 3
        new_x1 = {'lambda': new_x1_lambda, 'value': new_x1_value}
        new_x2 = {'lambda': new_x2_lambda, 'value': new_x2_value}
        if f_x1 > f_xm:
            if f_x2 > f_xm:
                a = new_x1
                b = new_x2
            else:
                a = x_m
                x_m = new_x2
        else:
            b = x_m
            x_m = new_x1
        k += 1


def get_x(x, s, delta):
    return x + s * delta


def norm(array):
    return math.sqrt(sum([value ** 2 for value in array]))


def get_lambda(x, s):
    return 0.00001 * (norm(x) / norm(s))


def golden_ratio(par_function, interval, s, epsilon):
    a = interval[0]
    b = interval[2]

    x1_lambda = 0.382 * (b['lambda'] - a['lambda']) + a['lambda']
    x1_value = a['value'] + numpy.array([0.382, 0.382]) * (b['lambda'] - a['lambda']) * s
    x1 = {'lambda': x1_lambda, 'value': x1_value}
    x2_lambda = 0.618 * (b['lambda'] - a['lambda']) + a['lambda']
    x2_value = a['value'] + numpy.array([0.618, 0.618]) * (b['lambda'] - a['lambda']) * s
    x2 = {'lambda': x2_lambda, 'value': x2_value}
    while True:
        L = b['lambda'] - a['lambda']
        if math.fabs(L) < epsilon:
            return x1
        f_x1 = f(par_function, x1['value'])
        f_x2 = f(par_function, x2['value'])
        if f_x1 <= f_x2:
            b = x2
            x2 = x1
            x1_lambda = 0.382 * (b['lambda'] - a['lambda']) + a['lambda']
            x1_value = a['value'] + numpy.array([0.382, 0.382]) * (b['lambda'] - a['lambda']) * s
            x1 = {'lambda': x1_lambda, 'value': x1_value}
        else:
            a = x1
            x1 = x2
            x2_lambda = 0.618 * (b['lambda'] - a['lambda']) + a['lambda']
            x2_value = a['value'] + numpy.array([0.618, 0.618]) * (b['lambda'] - a['lambda']) * s
            x2 = {'lambda': x2_lambda, 'value': x2_value}
