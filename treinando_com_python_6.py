'''
Data Scientist Jr.: Dr.Eddy Giusepe Chirinos Isidro

Link de estudo: https://www.youtube.com/watch?v=goFjfPklfcg
'''
class Fraction:
    def __init__(self, num = 0, den = 1):
        if isinstance(num, int):
            self.num = num
        else:
            self.num = 0
        if isinstance(den, int) and den != 0:
            self.den = den
        else:
            self.den = 1

    def imprime(self):
        print(self.num, "/", self.den)

    # Detrutor "__del__"
    # def __del__(self):
    #     print("Destruindo o objeto!", self.num, "/", self.den)

    # Método __mul__
    def __mul__(self, obj):
        n = self.num * obj.num
        d = self.den * obj.den
        x = Fraction(n, d)
        return x

    def __add__(self, obj):
        n = self.num * obj.den + self.den * obj.num
        d = self.den * obj.den
        x = Fraction(n, d)
        return x

    def igual(self, eddy):
        if self.num / self.den == eddy.num / eddy.den:
            return True
        else:
            return False

if __name__ == "__main__":
    a = Fraction(6, 8)
    b = Fraction(3, 4)
    a.imprime()
    b.imprime()
    r = a + b
    r.imprime()

    m = a * b
    m.imprime()

    print(a == b)