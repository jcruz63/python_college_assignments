from random import randrange


def atk_roll(base_attack):
    x = randrange(20)
    print(x + base_attack)


if __name__ == '__main__':
    atk_roll(4)
    atk_roll(5)
    atk_roll(6)
