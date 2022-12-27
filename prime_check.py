
from random import choice


def miller_rabin(n, k):
    '''
    Провереряет число на простоту с помощь алгоритма Миллер-Рабина
    :param n: Число, проверяемое на простоту
    :param k: Количество испытаний
    :return: True или False, зависит от простоты числа
    '''

    t = n - 1
    s = 0
    while t % 2 == 0:
        t //= 2
        s += 1

    for _ in range(k):
        a = choice(range(2, n - 2))
        x = pow(a, t, n)
        if x == 1 or x == n - 1:
            continue

        for __ in range(s - 1):
            x = x ** 2 % n
            if x == 1:
                return False
            if x == n - 1:
                break
        if x == n - 1:
            continue
        return False
    return True

class fun_test():
    def __init__(self, tests, func):
        self.tests = tests
        self.func = func
        self.results = []

    def check(self, condition_cheked=lambda x, y, z: y == z):
        
        self.results.clear()
        for test in self.tests:
            returned = self.func(*test[0])
            self.results.append((test[0], returned,
                                 condition_cheked(test[0], returned, test[1])))



    def print_result(self):
        
            count = 1
            print('Testing start\n'
                  f'function: {self.func.__name__}\n')
            for result in self.results:
                if result[2] == 0:
                    print(f'Test {count}: '
                          f'input: {result[0]}\n'
                        f'returned: {result[1]}\n'
                        f'correctness: Fail\n')
                else:
                    print(f'Test {count}: '
                          f'input: {result[0]}\n'
                        f'returned: {result[1]}\n'
                        f'correctness: Done\n')
                count += 1
            print('Testing finished\n')

tests = [((321197185, 10), False),
         ((9746347772161, 10), False),
         ((104729, 10), True),
         ((13466917, 10), True)]

miller_rabin_test = fun_test(tests, miller_rabin)
miller_rabin_test.check()
miller_rabin_test.print_result()
