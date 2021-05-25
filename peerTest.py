import math


def my_sqrt(a):
    x = a

    while True:

        y = (x + a / x) / 2.0

        if y == x:
            break

        x = y

    return y


def test_sqrt():
    for a in range(1000, 1020):
        approxsqrt = my_sqrt(a)

        actualsqrt = math.sqrt(a)

        print("a =", a,

              "approx. sqrt =", approxsqrt,

              "actual sqrt =", actualsqrt,

              "difference =", abs(approxsqrt - actualsqrt))


def main():
    test_sqrt()


main()
