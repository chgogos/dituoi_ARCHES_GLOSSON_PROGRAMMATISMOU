# Δημιουργία "άπειρης" ακολουθίας Fibonacci με generator
def a_simple_generator():
    a = b = 1
    yield a
    yield b
    while True:
        yield a + b
        b += a
        a = b - a


gen = a_simple_generator()

for _ in range(20):
    print(next(gen))
