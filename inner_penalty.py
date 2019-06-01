import algorithm
from function import *

restriction1 = x
restriction2 = y
r_coeff = 1
function = fun
start_point = x0
c_coeff = 10
start_point = start_point
inverse_penalty_function = ((1 / restriction1) + (1 / restriction2))
logarithm_penalty_function = (sympy.log(-restriction1) + sympy.log(-restriction2))

criterion = f(inverse_penalty_function, start_point)
new_point = start_point
while True:
    penalty_function = inverse_penalty_function
    new_point = algorithm.start(fun + r_coeff * inverse_penalty_function, new_point, draw=False, real_point=[0, 0],
                                print_output=True)
    if r_coeff < 0.01:
        break
    r_coeff /= c_coeff



print("--------------")
print(new_point)
print(f(fun, new_point))
