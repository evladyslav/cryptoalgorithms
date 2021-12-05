from random import randint, choice
from simple_digits import simple_dig


def analyze(p_r):
    c = 0
    d = 0
    for i in range(1, 1000):
        c = randint(3, 19)
        d = randint(3, 19)
        if c * d % (p_r-1) == 1:
            break
    return [c, d]


if __name__ == '__main__':
    status = "0"

    # p = 19  # ПРОСТОЕ ЧИСЛО  int(input('Input p: '))
    while status == '0':
        simple_digits = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
        p = choice(simple_digits[:7])
        #n = randint(2, 2 ** 8)
        #print(n)
        #p = simple_dig(n)
        # ca, da, cb, db = 0, 0, 0, 0
        # while ca == da or cb == db or da == db or ca == cb:  # or da == db:
        ca, da = analyze(p)
        cb, db = analyze(p)

        m = randint(2, p-1)
        x_1 = (m ** ca) % p
        x_2 = (x_1 ** cb) % p

        x_3 = (x_2 ** da) % p
        x_4 = (x_3 ** db) % p

        if x_4 == m and not x_1 == m and not x_2 == m and not x_3 == m:
            status = "OK"
            print(f'p= {p} \nCa = {ca} \nDa = {da}\nCb = {cb} \nDb = {db}\nm = {m}')
            print(f'x_1 = {m} ^ {ca} mod({p}) = {x_1}')
            print(f'x_2 = {x_1} ^ {cb} mod({p}) = {x_2}')
            print(f'x_3 = {x_2} ** {da} mod({p}) = {x_3}')
            print(f'x_4 = {x_3} ** {db} mod({p}) = {x_4}')
            break
        # print(status)