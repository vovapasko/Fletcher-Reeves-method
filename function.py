from data import *


def f(function, point):
    val = function.subs({x: point[0], y: point[1]})
    return function.subs({x: point[0], y: point[1]})
