from ast import Num
from cgi import print_environ_usage
from sympy import fraction

# Vamos criar uma classe para ler frações e multiplicar duas delas
class Fraction:
    num = 0
    den = 1
    
    def __init__(self, num = 0, den = 1):
        self.num = num
        self.den = den

    def multiplication_two_fractions(self, b):
        num = self.num*b.num
        den = self.den*b.den 
        r = Fraction(num, den)
        return r

    def print_out(self):
        print(self.num, "/", self.den)

fraction_a = Fraction(3, 2)
fraction_a.print_out()
fraction_b = Fraction(1, 5)
fraction_b.print_out()

r = fraction_a.multiplication_two_fractions(fraction_b)
r.print_out()





             

