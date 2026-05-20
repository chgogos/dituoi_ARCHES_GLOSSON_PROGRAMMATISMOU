import math


def f1(x):
    return x


def f2(x):
    return x * x


def f3(x):
    return x * x * x


def trapezio(a, b, n, fp):
    h = (b - a) / n
    approx = (fp(a) + fp(b)) / 2.0
    for i in range(1, n):
        x_i = a + i * h
        approx += fp(x_i)
    approx *= h
    return approx


def main():
    n = 1000000
    a, b = 0.0, 10.0

    approx = trapezio(a, b, n, f1)
    print(f"result: {approx:.5f}")
    approx = trapezio(a, b, n, f2)
    print(f"result: {approx:.5f}")
    approx = trapezio(a, b, n, f3)
    print(f"result: {approx:.5f}")
    approx = trapezio(a, b, n, math.exp)
    print(f"result: {approx:.5f}")
    approx = trapezio(a, b, n, math.sqrt)
    print(f"result: {approx:.5f}")


if __name__ == "__main__":
    main()
