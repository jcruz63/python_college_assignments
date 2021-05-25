import collections


def is_equivalent_or_identical(list_a, list_b):
    if list_a is list_b:
        print("list are identical, you should avoid alias")
    elif collections.Counter(list_a) == collections.Counter(list_b):
        print("list are equivalent")
    else:
        print("list are not identical or equivalent")


def filter_even(a_list):
    filtered_list = []
    for elem in a_list:
        if elem % 2 == 0:
            filtered_list.append(elem)
    print(f'original list {a_list} filtered elements {filtered_list}')
    return filtered_list


def map_power_second(a_list):
    twos_power_list = []
    for elem in a_list:
        twos_power_list.append(elem * elem)
    print(f'list elements raised to the second power {twos_power_list}')
    return twos_power_list


def filter_map_reduce(a_list):
    return sum(map_power_second(filter_even(a_list)))


def main():
    a_list = [1, 2, 3, 4, 5, 6]  # List A and B are equivalent
    b_list = [6, 5, 4, 3, 2, 1]
    c_list = a_list  # List C is identical to A and is also an alias. C is a reference to A
    d_list = [5, 6, 7, 9]  # List D is not identical or equivalent to list A, B, or C

    print("Comparing A list to B should return equivalent")
    is_equivalent_or_identical(a_list, b_list)
    print("\n")

    print("Comparing A list to C should return identical")
    is_equivalent_or_identical(a_list, c_list)
    print("\n")

    print("Comparing B list to C should return equivalent")
    is_equivalent_or_identical(b_list, c_list)
    print("\n")

    print("Comparing A list to D they are not identical or equivalent")
    is_equivalent_or_identical(a_list, d_list)
    print("\n")

    print("Comparing B list to D they are not identical or equivalent")
    is_equivalent_or_identical(b_list, d_list)
    print("\n")

    print("ouput to filter_map_reduce")
    print(filter_map_reduce(a_list))


main()
