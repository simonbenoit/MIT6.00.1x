def genPrimes():
    x = 2
    primes = set()
    while True:
        for p in primes:
            if x % p == 0:
                break
        else:
            primes.add(x)
            yield x
        x += 1