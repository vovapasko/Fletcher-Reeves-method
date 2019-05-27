import math
import numpy as np
import sympy
from sympy import diff
from function import *


def count_grad(point, x, y):
    diff_f_x = sympy.diff(fun, x)
    diff_f_y = sympy.diff(fun, y)
    f_x_point = diff_f_x.subs({x: point[0], y: point[1]})
    f_y_point = diff_f_y.subs({x: point[0], y: point[1]})
    return np.array([f_x_point, f_y_point])


def minus_vector(vector):
    return [-x for x in vector]


def transpose(matrix):
    arr = np.array(matrix)[np.newaxis]
    return arr.T


def find_hessian(fun, x0, x, y):
    print("---------------")
    print("Counting hessian")
    print(fun)
    print(x0)
    f_xx = sympy.diff(fun, x, 2)
    print("diff(f, x, 2) =", f_xx)
    f_xy = diff(diff(fun, x), y)
    print("diff(f, (x,y), 2) =", f_xy)
    f_yy = diff(fun, y, 2)
    print("diff(f, y, 2) =", f_yy)
    hess = [
        [f_xx.subs({x: x0[0], y: x0[1]}), f_xy.subs({x: x0[0], y: x0[1]})],
        [f_xy.subs({x: x0[0], y: x0[1]}), f_yy.subs({x: x0[0], y: x0[1]})]
    ]
    print(hess)
    print("---------------")
    return hess


def normalize(vector):
    a1 = norm(vector)
    res = vector / norm(vector)
    return vector / norm(vector)


def sven(x, s):
    llambda = get_lambda(x, s)
    x0_minus = get_x(x, s, -llambda)
    x0_plus = get_x(x, s, llambda)
    k = 1
    i = 0
    fc = 0
    x_values = []
    fminus = f(x0_minus)
    fc += 1
    fplus = f(x0_plus)
    fc += 1
    if fminus < fplus:
        llambda = -llambda
        x_values.append({'lambda': llambda, 'value': x0_minus})
    else:
        x_values.append({'lambda': llambda, 'value': x0_plus})
    while True:
        new_lambda = x_values[i]['lambda'] + (2 ** k) * llambda
        xk_next = get_x(x, s, new_lambda)
        fk = f(x_values[i]['value'])
        fc += 1
        fk_next = f(xk_next)
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


def dichotomy(point, interval, s, epsilon):
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
        f_x1 = f(new_x1_value)
        f_xm = f(x_m['value'])
        f_x2 = f(new_x2_value)
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
    return 0.1 * (norm(x) / norm(s))


def dsk(point, interval, s):
    a = interval[0]
    xm = interval[1]
    b = interval[2]
    new_x_lambda = xm["lambda"] + (
            ((f(a['value']) - f(b['value'])) * abs(xm['lambda'] - a["lambda"])) /
            (2 * (f(a['value']) - 2 * f(xm['value']) + f(b['value']))))

    new_x_value = get_x(point, s, new_x_lambda)
    new_x = {'lambda': new_x_lambda, 'value': new_x_value}
    a['f(x)'] = f(a['value'])
    xm['f(x)'] = f(xm['value'])
    b['f(x)'] = f(b['value'])
    new_x['f(x)'] = f(new_x['value'])
    return [a, xm, b, new_x]


def dsk_powell(point, interval, s):
    dsk_points = dsk(point, interval, s)
    dsk_sorted_points = sorted(dsk_points, key=lambda value: value['lambda'])
    sorted_points = dsk_sorted_points
    new_array = sorted_points[1:]
    min_point = new_array[0]
    a1 = (new_array[1]["f(x)"] - new_array[0]["f(x)"]) / (
            new_array[1]["lambda"] - new_array[0]["lambda"])
    a2 = (((new_array[2]["f(x)"] - new_array[0]["f(x)"]) / (
            new_array[2]["lambda"] - new_array[0]["lambda"])) - a1) / (
                 new_array[2]["lambda"] - new_array[1]["lambda"])
    new_x_lambda = (new_array[0]["lambda"] + new_array[1]["lambda"]) / 2 - (a1 / (2 * a2))
    new_x_value = get_x(point, s, new_x_lambda)
    return {'lambda': new_x_lambda, 'value': new_x_value, 'f(x)': f(new_x_value)}


def golden_ratio(interval, s, epsilon):
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
        f_x1 = f(x1['value'])
        f_x2 = f(x2['value'])
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
