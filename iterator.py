class Pell:
    """По объектам этого класса можно итерироваться и получать числа Пелля"""

    class _Pell_iter:
        """Внутренний класс — итератор"""
        def __init__(self):
            self.i = 0
            self.pells = [0, 1] # первые два числа Пелля
        
        def __next__(self):
            if self.i == 0:
                self.i += 1
                return 0
            elif self.i == 1:
                self.i += 1
                return 1
            else:
                j = self.i
                self.i += 1
                p = 2 * self.pells[j-1] + self.pells[j-2]
                self.pells.append(p)
                return p

    def __iter__(self):
        """Создать и вернуть итератор"""
        return Pell._Pell_iter()


pell_nums = Pell()
for i, num in enumerate(pell_nums):
    print(num)
