import math

def is_triangular(n):
    t = (-1 + math.sqrt(1 + 8 * n)) / 2
    return t.is_integer()

def is_square(x):
    return math.isqrt(x) ** 2 == x

def find_special_numbers(limit):
    for i in range(2, limit):
        if is_triangular(i - 2) and is_square(i + 2):
            print(i)

# Set a reasonable limit for demonstration purposes
limit = 1000000000000000000000000000000000
find_special_numbers(limit)
