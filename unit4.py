def is_divisible(x, y):
    return x % y == 0


def is_power(a, b):
    if a == 1 or a == b:
        return True
    elif b == 1 or not is_divisible(a, b):
        return False
    return is_power(a/b, b)


def main():
    print("is_power(10, 2) returns: ", is_power(10, 2))
    print("is_power(27, 3) returns: ", is_power(27, 3))
    print("is_power(1, 1) returns: ", is_power(1, 1))
    print("is_power(10, 1) returns: ", is_power(10, 1))
    print("is_power(3, 3) returns: ", is_power(3, 3))


main()

