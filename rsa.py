from random import randint
from sympy import nextprime


class RSA:
    def __init__(self):
        self.p = 0
        self.q = 0
        self.n = 0
        self.e = 0
        self.d = 0

        self.e_func = 0


    def extended_gcd(self, a, b):  
        if b == 0:  
            return 1, 0  
        else:  
            x1, y1 = self.extended_gcd(b, a % b)  
            x = y1  
            y = x1 - (a // b) * y1  
            return x, y


    def generate_primes(self):
        self.p = nextprime(randint(10000, 99999))
        self.q = nextprime(randint(10000, 99999))

        self.n = self.p*self.q


    def calc_e_func(self):
        self.e_func = (self.p -1)*(self.q - 1)


    def calc_e(self):
        e = nextprime(randint(self.e_func//5, self.e_func//2))

        if self.nod(e, self.e_func) != 1 or e > self.e_func:
            return self.calc_e()
        else:
            self.e = e


    def calc_d(self):
        x, y = self.extended_gcd(self.e_func, self.e)

        self.d = self.e_func - abs(x) if x < y else self.e_func - abs(y)


    def nod(self, a, b):
        remains = a % b if a >= b else b % a
        if remains == 0:
            return b if a >= b else a
        else:
            return self.nod(remains, b) if a >= b else self.nod(a, remains)

    
    def generate_keys(self):
        self.generate_primes()
        self.calc_e_func()
        self.calc_e()
        self.calc_d()
        return (self.e, self.n), (self.d, self.n)