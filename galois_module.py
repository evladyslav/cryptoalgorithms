from math import gcd
from random import randint


def is_coprime(x, y):
    return gcd(x, y) == 1


def galois_f(q):
    galois_field = [x for x in range(1, q+1)]
    euler = []
    full_state = set(galois_field[:-1])
    for i in range(1, q-1):
        if is_coprime(i, q-1):
            euler.append(i)
    groups = []
    g = []
    for i in range(2, q - 1):
        group = ''
        states = [(i ** x) % q for x in range(q-1)]
        states_set = set(states)
        if states_set == full_state:
            for j in range(q):
                group += f'{i}^{j} = {(i ** j) % q}, '
            groups.append([group])
            g.append(i)
    return [galois_field, euler, groups, g]


def galois_generator(q):
    galois_field = [x for x in range(1, q+1)]
    euler = []
    full_state = set(galois_field[:-1])
    for digit in range(1, q-1):
        if is_coprime(digit, q-1):
            euler.append(digit)

    for gen in range(2, q):
        states = [(gen ** grade) % q for grade in range(q-1)]
        states_set = set(states)
        if states_set == full_state:
            return gen
