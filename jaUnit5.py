def word_builder():
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'
    for letter in prefixes:
        if letter == "O" or letter == "Q":
            print(letter + "u" + suffix)
        else:
            print(letter + suffix)


class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def print_name(self):
        print("{last}, {first}".format(last=self.lastname, first=self.firstname))


def fullname_to_first_and_last(fullname):
    space = fullname.find(" ")
    if space == -1:
        print("Invalid name input name must be in the form of first last")
        return -1
    else:
        return Person(fullname[0:space], fullname[space + 1:len(fullname)])


def string_splitter(mystring):
    space = mystring.find(" ")
    words = []
    substr = mystring
    while space != -1:
        words.append(substr[0: space])
        substr = substr[space + 1: len(substr)]
        space = substr.find(" ")
    words.append(substr)
    return words


def string_reverse(astring):
    chars = []
    counter = len(astring) - 1
    while counter >= 0:
        chars.append(astring[counter])
        counter -= 1
    return "".join(chars)


def main():
    print("OUTPUT: Word builder")
    word_builder()
    print("OUTPUT: fullname_to_first_and_last")
    fullname_to_first_and_last("Jonathan Cruz").print_name()
    print("OUTPUT: string_splitter")
    print(string_splitter("Mary had a little lamb"))
    print("OUTPUT: string_reverse")
    print(string_reverse("hello world"))
    print("OUTPUT: passing string_reverse to splitter")
    print(string_splitter(string_reverse("Mary had a little lamb")))


main()
