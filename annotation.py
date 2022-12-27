from typeguard import typechecked


@typechecked
def gcd(a: int, b: int) -> int:
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


try:
    a = 10
    b = 20
    print(f'НОД(a, b) = {gcd(a, b)}')
    print('Тест 1 -- целые числа можно')
except:
    print('Тест 1 -- целые числа нельзя')

try:
    a = '10'
    b = 20
    print(f'НОД(a, b) = {gcd(a, b)}')
    print('Тест 2 -- строки можно')
except:
    print('Тест 2 -- строки нельзя')
try:
    a = 10.23
    b = 20
    print(Euclid_algorithm(a, b))
    print('Тест 3 -- вещественные числа можно')
except:
    print('Тест 3 -- вещественные числа нельзя')
try:
    a = 10
    b = [20.0]
    print(f'НОД(a, b) = {gcd(a, b)}')
    print('Тест 4 -- список можно')
except:
    print('Тест 4 -- список нельзя')
