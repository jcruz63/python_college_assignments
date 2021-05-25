def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n - 1)


def countup(n):
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n + 1)


if __name__ == '__main__':

    userInput = int(input("Please input count"))

    if userInput > 0:
        countdown(userInput)
    elif userInput < 0:
        countup(userInput)
    else:
        raise RuntimeError("zero is not a valid input")
