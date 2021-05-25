# basic linear interpolation

def lerp_step1(min, max, norm):
    return 0

def lerp_step2(min, max, norm):
    r = max - min
    print("range is:", r)
    return 0


def lerp_step3(min, max, norm):
    r = max - min
    if 0 < norm <= 1:  # check if value is normalized
        t = r * norm
        print(t)
    return 0

def lerp_step4(min, max, norm):
    r = max - min
    if 0 < norm <= 1:
        t = r * norm
        return t + min  # we add min value back as an offset from zero
    else:
        print("per must be great than 0 and less than or equal to 1.0")
    return -1  # negative one is to symbol error



def main():
    max = 450
    min = 100
    print("return of step 1 ->", lerp_step1(min, max, .37))
    print("return of step 2 ->", lerp_step2(min, max, .37))
    print("return of step 3 ->", lerp_step3(min, max, .37))
    print("return of step 4 ->", lerp_step4(min, max, .37))
    print(lerp_step4(3, 4, .3))
    print(lerp_step4(56, 89, .2))
    print(lerp_step4(89, 134, .9))


main()

