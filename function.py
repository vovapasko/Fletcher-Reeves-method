import numpy
import sympy

x, y = sympy.symbols('x y ')

fun_test1 = x ** 2 + x * y + 6 * y ** 2
real_min_fun_test1 = [0, 0]

f_test = x ** 2 + 4 * x + 6 * y ** 2
real_min_point_test = [-2, 0]

point_test = numpy.array([4, 3])

f1 = (1 - x) ** 2 + 100 * (y ** 2 - 2 * (x ** 2) * y + x ** 4)
x01 = numpy.array([-1.2, 0.0])
real_minx01 = [1, 1]

f2 = ((10 * (x - y)) ** 2 + (x - 1) ** 2) ** 4
x02 = numpy.array([-1.2, 0.0])
real_minx02 = [1, 1]

fun = f1
x0 = x01
real_min_point = real_minx01


def f(point):
    return fun.subs({x: point[0], y: point[1]})
