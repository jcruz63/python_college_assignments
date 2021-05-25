def string_split(a_string):
    if isinstance(a_string, str):
        return a_string.split()
    else:
        return []


def list_delete_three(a_list):
    # this is done to keep the function pure by not modifying the original list
    copy_list = a_list.copy()
    # checking length of list to ensure it is long enough to remove three elements
    if len(copy_list) >= 3:
        copy_list.remove(a_list[0])
        del copy_list[0]
        # pop returns the element I am explicitly ignoring the return
        copy_list.pop(0)
        return copy_list
    else:
        return []


def list_sort(a_list):
    # this is done to keep the function pure by not modifying the original list
    copy_list = a_list.copy()
    if len(copy_list) > 0:
        copy_list.sort()
        return copy_list
    else:
        return copy_list


def list_add_three(a_list, elem1, elem2, b_list):
    # this is done to keep the function pure by not modifying the original list
    copy_list = a_list.copy()
    copy_list.append(elem1)
    copy_list.insert(1, elem2)
    copy_list.extend(b_list)
    return copy_list


def list_to_string(a_list):
    separator = " "
    return separator.join(a_list)


def combined_operations(a_string, word1, word2, a_list_of_words):
    print(list_to_string(
        list_delete_three(
            list_add_three(
                list_sort(string_split(a_string)), word1, word2, a_list_of_words))))


def filter_even(a_list):
    filtered_list = []
    for elem in a_list:
        if elem % 2 == 0:
            filtered_list.append(elem)
    print(f'original list {a_list} filtered elements {filtered_list}')
    return filtered_list


def main():
    my_string = "The end of days"
    word1 = "Hello"
    word2 = "World"
    my_list = ["cat", "dog"]
    combined_operations(my_string, word1, word2, my_list)
    nested_list = [my_list * 2, string_split(my_string)]
    print(nested_list)
    print(my_list * 3)
    print(string_split(my_string)[1:2])
    nested_list += my_list
    print(nested_list)

    numbers = [5, 6, 7, 8]
    print(filter_even(numbers))


main()
