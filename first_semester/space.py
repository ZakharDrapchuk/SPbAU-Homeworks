class Deduction:
    def __init__(self, numb, base, res):
        """
       Опишем класс кольца вычетов по модулю
       Параметры:
       numb:
          число, которое будем рассматривать в кольце
       base:
          основание кольца вычетов
       res:
          остаток от деления numb и base
        """
        self.numb = numb
        self.base = base
        self.res = res

    def great_common(self):
        """
        Функция для поиска остатка от деления
        """
        self.res = self.numb
        while self.res >= self.base:
            self.res -= self.base
        return self.res

    def __add__(self, other):
        """
       Функция для сложения
       """
        return Deduction(self.numb + other.numb, self.base, (self.numb + other.numb) % self.base)

    def __sub__(self, other):
        """
        Функция для вычитания
        """
        ded = self.res - other.res
        if ded < 0:
            ded += self.base
        return Deduction(self.numb - other.numb, self.base, ded)

    def __mul__(self, other):
        """
        Функция для умножения
        """
        result_mul = self.numb * other.numb
        return Deduction(result_mul, self.base, result_mul % self.base)

    def __truediv__(self, other):
        """
        Функция для деления
        """
        if other.numb == 0:
            raise ZeroDivisionError
        if self.numb % other.numb != 0:
            raise RuntimeError
        result_div = self.numb / other.numb
        return Deduction(result_div, self.base, result_div % self.base)

    def __str__(self):
        """
        Функция для преобразования числа в строку
        """
        return str(self)

    '''Тесты'''


def test_deduction():
    # создаем объекты класса Deduction
    d1 = Deduction(10, 5, 0)
    d2 = Deduction(7, 5, 0)
    # проверяем метод great_common
    assert d1.great_common() == 0
    assert d2.great_common() == 2
    # проверяем операторы сложения, вычитания и умножения
    assert (d1 + d2).res == 2
    assert (d1 - d2).res == 3
    assert (d1 * d2).res == 0
    # проверяем оператор деления
    d3 = Deduction(15, 5, 0)
    d4 = Deduction(3, 5, 0)
    try:
        d3 / d4
    except ZeroDivisionError:
        pass
    except RuntimeError:
        assert False, "Expected ZeroDivisionError"
    d5 = Deduction(8, 5, 0)
    d6 = Deduction(3, 5, 0)
    try:
        d5 / d6
    except RuntimeError:
        pass
    else:
        assert False, "Expected RuntimeError"
    assert (d5 / Deduction(2, 5, 0)).res == 4
    return 'Тест пройден.'


print(test_deduction())
