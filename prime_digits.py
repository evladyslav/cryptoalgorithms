def simple_dig(n):
    sieve = list(range(n**2 + 1))

    sieve[1] = 0
    for i in range(len(sieve)):
        if sieve[i] > 1:
            for j in range(i ** 2, len(sieve), i):
                sieve[j] = 0
            i += 1
        else:
            i += 1

    sieve = [dig for dig in sieve if dig != 0]# [:n+1]

    return sieve[n-1]




