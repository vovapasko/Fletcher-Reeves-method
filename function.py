from data import *


def f(function, point):
    return function.subs({x: point[0], y: point[1]})
