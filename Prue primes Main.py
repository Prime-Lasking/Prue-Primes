import math
import Functions as f
import time as t
start_time=t.time()
n = 100000000000000000
for i in range(5, n, 6):
    if f.is_triangular(i - 2) and f.is_square(i + 2) and f.is_prime_fermat(i):
        print(i)
    if f.is_triangular(i + 1) and f.is_square(i + 3) and f.is_prime_fermat(i + 2):
        print(i + 2)
end_time=t.time()
elapsed_time = end_time - start_time
print(f"Solved in {elapsed_time:.10f} seconds!")