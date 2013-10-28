from math import sqrt

def fib(nth):
    i, j = 0, 1
    for _ in xrange(nth):
        i, j = j, i+j
    return i

def fib2(nth):
    bigphi = (1+sqrt(5)) / 2
    miniphi = (1-sqrt(5)) / 2
    return int((bigphi**nth - miniphi**nth) / sqrt(5))

def fib3(nth):
    from decimal import Decimal as D
    sqrt5 = D(5).sqrt()
    bigphi = (1 + sqrt5) / 2
    return int((bigphi**nth / sqrt5).to_integral())

if __name__ == "__main__":
    with open('py.fib', 'w') as f:
        f.write(str(fib(4374897)))
