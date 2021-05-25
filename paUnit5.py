import math


def my_sqrt(a):
    x = 9
    while True:
        y = (x + a / x) / 2
        if y == x:
            break
        x = y
    return x


def print_results(count, func1, func2, diff):
    print("a = {a} | my_sqrt(a) = {b} | math.sqrt(a) = {c} | diff = {d}".format(a=count, b=func1, c=func2, d=diff))


def test_sqrt(iterations):
    count = 1
    while iterations >= count:
        result1 = my_sqrt(count)
        result2 = math.sqrt(count)
        print_results(count, result1, result2, abs(result1 - result2))
        count += 1


def main():
    test_sqrt(25)


main()
