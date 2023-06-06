def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_generator(n):
    primes = [2]
    num = 3
    count = 1
    while count <= n:
        if all(num % prime != 0 for prime in primes):
            primes.append(num)
            count += 1
        num += 2
    return primes

n = int(input("Enter the number of prime numbers to generate: "))
primes = prime_generator(n)
for prime in primes:
    print(prime)
