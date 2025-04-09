import random
import math
def is_prime_fermat(n, k=5):
    if n % 2 == 0:
        return "not prime"
    if n <= 1:
        return "not prime"
    if n <= 3:
        return "prime"
    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
    return True

def is_triangular(n):
    t = (-1 + math.sqrt(1 + 8 * n)) / 2
    return t.is_integer()

def is_square(x):
    return math.isqrt(x) ** 2 == x
