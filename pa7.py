alphabet = "abcdefghijklmnopqrstuvwxyz"

test_dups = ["zzz", "dog", "bookkeeper", "subdermatoglyphic", "subdermatoglyphics"]

test_miss = ["zzz", "subdermatoglyphic", "the quick brown fox jumps over the lazy dog"]


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def has_duplicates(a_string):
    histo = histogram(a_string)
    for value in histo:
        if histo[value] > 2:
            return True
    return False


def missing_letters(a_string):
    missing = []
    for c in alphabet:
        if a_string.find(c) == -1:
            missing.append(c)
    return f'This string "{a_string}" does not contain the following letters from the alphabet: {missing}'


if __name__ == '__main__':
    print("testing duplicates \n")
    for s in test_dups:
        print(f'The string: "{s}" has duplicates: {has_duplicates(s)}')
    print("\n testing missing letters \n")
    for s in test_miss:
        print(missing_letters(s))
