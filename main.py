import math
import numpy
from tools import *
from function import *


epsilon = 0.01
epsilon_dich = 0.001
s0 = -normalize(count_grad(x0, x, y))
s = [s0]
x_values = [x0]
i = 0

while True:
    print("i = ", i)
    sven_interval = sven(x_values[i], s[i])
    point = dichotomy(x_values[i], sven_interval, s[i], epsilon_dich)
    # point = dsk_powell(x_values[i], sven_interval, s)
    llambda = point['lambda']
    new_x = x_values[i] + llambda * s[i]
    x_values.append(new_x)
    print("(x, y) = ", x_values[-1])
    print("f(x, y) =", f(x_values[-1]))
    if norm(count_grad(new_x, x, y)) <= epsilon:
        print("Search is finished")
        break

    a = -count_grad(x_values[i], x, y)
    b = (norm(count_grad(x_values[i], x, y)) ** 2)
    c = (norm(count_grad(x_values[i - 1], x, y)) ** 2)
    new_s = a + s[i] * b / c

    new_s = normalize(new_s)
    s.append(new_s)
    i += 1
    print("-------------------")

print("(x, y) = ", x_values[-1])
print("f(x, y) =", f(x_values[-1]))
