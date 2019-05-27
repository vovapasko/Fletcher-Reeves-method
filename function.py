import numpy
import sympy

x, y = sympy.symbols('x y ')
# fun = x ** 2 + y ** 2
f_test = x ** 2 + 4 * x + 6 * y ** 2
point_test = numpy.array([4, 3])

f1 = (1 - x) ** 2 + 100 * (y ** 2 - 2 * (x ** 2) * y + x ** 4)
x01 = numpy.array([-1.2, 0.0])

f2 = ((10 * (x - y)) ** 2 + (x - 1) ** 2) ** 4
x02 = numpy.array([-1.2, 0.0])

f3 = (10 * (x - y) ** 2 + (x - 1) ** 2) ** (1 / 4)
x03 = numpy.array([-1.2, 0.0])

fun = f_test
x0 = point_test


def f(point):
    return fun.subs({x: point[0], y: point[1]})
