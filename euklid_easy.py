a, b = map(int, input('Введите челые числа a и b через пробел: ').split())

def gcd(a, b):

    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b 
    
print(f'НОД(a, b) = {gcd(a, b)}')
