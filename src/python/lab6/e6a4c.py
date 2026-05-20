import time
from functools import cache


@cache
def fibonacci_cached(n):
    if n <= 1:
        return n
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)

n = 50
start = time.perf_counter()
result = fibonacci_cached(n)
elapsed = time.perf_counter() - start

print(f"With cache: n={n}, fib={result}, time={elapsed:.8f} sec")
