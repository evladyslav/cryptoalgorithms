from math import gcd
from random import randint


def is_coprime(x, y):
    return gcd(x, y) == 1


def galois_f(q):
    galois_field = [x for x in range(1, q+1)]
    eyler = []
    test = set(galois_field[:-1])
    for i in range(1, q-1):
        if is_coprime(i, q-1):
            eyler.append(i)
    groups = []
    g = []
    for i in range(2, q - 1):
        group = ''
        minimal = [(i ** x) % q for x in range(q-1)]
        t = set(minimal)
        if t == test:
            for j in range(q):
                group += f'{i}^{j} = {(i ** j) % q}, '
            groups.append([group])
            g.append(i)
    return [galois_field, eyler, groups, g]


def min_galois(q):
    galois_field = [x for x in range(1, q+1)]
    eyler = []
    test = set(galois_field[:-1])
    for i in range(1, q-1):
        if is_coprime(i, q-1):
            eyler.append(i)

    for i in range(2, q):
        minimal = [(i ** x) % q for x in range(q-1)]
        t = set(minimal)

        if t == test:
            return i
