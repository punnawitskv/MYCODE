def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_relative_primes():
    relative_primes = []
    for n in range(1, 151):
        if not is_prime(n) and n % 2 != 0 and n % 5 != 0 and n % 7 != 0:
            relative_primes.append(n)
    return relative_primes

print(find_relative_primes())
