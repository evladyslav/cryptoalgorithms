from random import randint, choice
from simple_digits import simple_dig
from os import urandom


def my_random(b):
    x = randint(2, b)
    return x


def analyze(p_):
    c = 0
    d = 0
    for i in range(1, 1000):
        c = randint(2, 2**8)
        d = randint(2, 2**8)
        if c * d % (p_-1) == 1:
            break
    return [c, d]


def encrypt(a, b, c):
    x = (a ** b) % c
    return x


if __name__ == '__main__':
    status = "0"

    n = randint(2, 2 ** 8)

    p = simple_dig(n)

    ca, da = analyze(p)
    cb, db = analyze(p)

    # m = randint(2, p-1)

    x_1 = (m ** ca) % p
    x_2 = (x_1 ** cb) % p

    x_3 = (x_2 ** da) % p
    x_4 = (x_3 ** db) % p

    print(f'p= {p} \nCa = {ca} \nDa = {da}\nCb = {cb} \nDb = {db}\nm = {m}')
    print(f'x_1 = {m} ^ {ca} mod({p}) = {x_1}')
    print(f'x_2 = {x_1} ^ {cb} mod({p}) = {x_2}')
    print(f'x_3 = {x_2} ** {da} mod({p}) = {x_3}')
    print(f'x_4 = {x_3} ** {db} mod({p}) = {x_4}')
