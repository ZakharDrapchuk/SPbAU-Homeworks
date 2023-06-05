import math
from typeguard import typechecked


@typechecked
def check(num):
     if math.factorial(num - 1) % -num == -1:
        return f'число {num} простое'
     else:
        return f'Число {num} составное'


test_cases = [5, 7, 10, '12', 3.14, [2, 3, 5], 3.11 - 12j]

for num in test_cases:
    try:
        result = check(num)
        print(f'Тест пройден. Результат: {result}')
    except:
        if type(num) == type('str'):
            print('Тест провален. Была введена строка.')
        elif type(num) == type(0.1):
            print('Тест провален. Было введено число с плавающей запятой.')
        elif  type(num) == type([1, 0]):
            print('Тест провален. Был введён список.')
        else:
            print('Тест провален. Недопустимый тип.')   
