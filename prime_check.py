
import math 
from sympy import isprime
#выпоним проверку при помощи т. Вильсона

def check(num):
     if math.factorial(num - 1) % -num == -1:
        return True #число простое
     else:
        return False #составное
     
'''Проверка'''

tests = [561, 1105, 1729, 191, 619, 977, 22, 111, 316]
results = []
symp_results = []

for i in range(0,9):
    results.append(check(tests[i]))
    symp_results.append(isprime(tests[i]))

if results == symp_results:
    print('Работает вполне неплохо')
else:
    print('Лучше попробовать другой алгоритм')
