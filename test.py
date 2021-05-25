def function2(param):
    print(param, param)


def function1(part1, part2):
    cat = part1 + part2
    function2(cat)


def main():
    chant1 = "See You "
    chant2 = "See Me "
    function1(chant1, chant2)


main()
