def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


import time

n = 0
while True:
    start = time.perf_counter()
    result = fibonacci(n)
    elapsed = time.perf_counter() - start

    print(f"n={n}, fib={result}, time={elapsed:.4f} sec")

    if elapsed > 10:
        break

    n += 1
