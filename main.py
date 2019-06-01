import algorithm
from function import *

restriction1 = x
restriction2 = y
r_coeff = 1
function = fun
start_point = numpy.array([3, 1.5])
c_coeff = 10
new_point = start_point

while r_coeff > 0.01:
    inverse_penalty_function = r_coeff * (restriction1 + restriction2)
    new_point = algorithm.start(fun + inverse_penalty_function, new_point, draw=False, real_point=[0, 0])
    r_coeff /= c_coeff