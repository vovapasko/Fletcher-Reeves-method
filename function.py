import sympy

x, y = sympy.symbols('x y ')
fun = x ** 2 + y ** 2


# fun = (1 - x) ** 2 + 100 * (y ** 2 - 2 * (x ** 2) * y + x ** 4)
# fun = x ** 2 + 4 * x + 6 * y ** 2

def f(point):
    return fun.subs({x: point[0], y: point[1]})
