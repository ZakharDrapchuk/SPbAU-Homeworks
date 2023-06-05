a, b = map(int, input('Введите челые числа a и b через пробел: ').split())

def egcd(a, b):
   
    if b == 0 :
        return (1, 0, a)
    y, x, gcd = egcd(b, a % b)
    return (x, y - (a // b) * x, gcd)

print(f'НОД(a, b) = {a}*{egcd(a, b)[0]} + {b}*{egcd(a, b)[1]} = {egcd(a, b)[2]}')    
