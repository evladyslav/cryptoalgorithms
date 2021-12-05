from random import randint
from galois_module import min_galois
from simple_digits import simple_dig
from argparse import ArgumentParser


def encrypt(m, p, g, x):
    k = 0
    y = (g ** x) % p
    Pkb = (p, g, y)
    enc = []
    t_enc = []
    while not k == x:
        k = randint(1, p - 1)
        c_1 = g ** k % p
        c_2 = y ** k % p
        for i in m:
            t_enc.append(c_2 * ord(i))
        size = len(str(max(t_enc)))
        for i in t_enc:
            enc.append(str(i).zfill(size))
        return enc, c_1


def decrypt(c_1, p, x, message):
    decryption = []
    for i in range(len(message)):
        msg = int(int(message[i]) / (c_1 ** x % p))
        decryption.append(chr(msg))
    return decryption


def main():
    m = "As ek in die kamer instap en daarna kyk, voel ek of dit wakker is. Ek het die dag nie opgelet nie, dis 'n wonderlike liggaam, soos 'n dans. Miskien 'n danstyd, altyd dans? Hoe kan ek"

    n = randint(2, 2 ** 8)

    try:
        p = simple_dig(n)
        g = min_galois(p)
        x = randint(2, p - 1)

        encrypted, c_1 = encrypt(m, p, g, x)
        decrypted = decrypt(c_1, p, x, encrypted)
        print(f'\nn = {n}\np = {p}; \ng = {g}; \nx = {x};')
        print('ШИФР:\n', ''.join(encrypted))
        print('РАСШИФРОВКА: \n', ''.join(decrypted))
    except IndexError as IU:
        print(f'Error n = {n}')


if __name__ == '__main__':

    main()
