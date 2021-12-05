from random import randint
from galois_module import galois_generator
from prime_digits import simple_dig


def encrypt(m, p, g, x):
    y = (g ** x) % p
    # Pkb = (p, g, y)
    encrypted = []
    t_enc = []
    k = randint(2, p - 1)
    c_1 = g ** k % p
    c_2 = y ** k % p
    for i in m:
        t_enc.append(c_2 * ord(i))
    size = len(str(max(t_enc)))
    for i in t_enc:
        encrypted.append(str(i).zfill(size))
    return encrypted, c_1


def decrypt(c_1, p, x, message):
    decrypted = []
    for i in range(len(message)):
        msg = int(int(message[i]) / (c_1 ** x % p))
        decrypted.append(chr(msg))
    return decrypted


def main():
    m = "Lorem ipsum dolor"
    n = randint(2, 2 ** 8)
    try:
        p = simple_dig(n)
        g = galois_generator(p)
        x = randint(2, p - 1)
        encrypted, c_1 = encrypt(m, p, g, x)
        decrypted = decrypt(c_1, p, x, encrypted)
        print(f'\nn = {n}\np = {p}; \ng = {g}; \nx = {x};')
        print('ШИФР:\n', ''.join(encrypted))
        print('РАСШИФРОВКА: \n', ''.join(decrypted))
    except IndexError as IE:
        print(f'n = {n}\n{IE}')


if __name__ == '__main__':
    main()
