class Calc:
    def get_minus(self, a, b):
        if a < b:
            return self.get_minus(b, a)
        return a - b

    def fibo(self, num):
        if num == 1 or num == 2:
            return 1

        return self.fibo(num - 1) + self.fibo(num - 2)

