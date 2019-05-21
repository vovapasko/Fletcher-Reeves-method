import math
import numpy
from tools import *
from function import *

x0 = numpy.array([4, 3])
epsilon = 0.01
epsilon_dich = 0.001
s0 = -count_grad(x0, x, y)
s = [s0]
x_values = [x0]
i = 0

while True:
    print("i = ", i)
    sven_interval = sven(x_values[i], s0)
    point = dichotomy(x_values[i], sven_interval, s[i], epsilon_dich)
    # point = dsk_powell(x_values[i], sven_interval, s)
    llambda = point['lambda']
    new_x = x_values[i] + llambda * s[i]
    x_values.append(new_x)
    print("(x, y) = ", x_values[-1])
    print("f(x, y) =", f(x_values[-1]))
    new_x_grad = count_grad(new_x, x, y)
    if normalize(count_grad(new_x, x, y)) <= epsilon:
        print("Search is finished")
        break
    new_s = -count_grad(new_x, x, y) + s[i] * ((normalize(count_grad(new_x, x, y)) ** 2) /
                                               (normalize(count_grad(x_values[i - 1], x, y)) ** 2))
    s.append(new_s)
    i += 1
    print("-------------------")

print("(x, y) = ", x_values[-1])
print("f(x, y) =", f(x_values[-1]))
