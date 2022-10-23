def isPrime(n):
    if(n < 2):
        return False
    d = 2
    while n % d != 0:
        d += 1
    return d == n