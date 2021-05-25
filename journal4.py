import math

# create function stub
def hyp_step1(a, b):
    return 0

# first second step square a and b print results to test
def hyp_step2(a, b):
    print("inside step 2")  # this is just to make the console read clearer
    a_sqr = a**2
    b_sqr = b**2
    print('a squared is', a_sqr)
    print('b squared is', b_sqr)
    return 0

#  third step get the sum of a and b square print to test
def hyp_step3(a, b):
    print("inside step 3")  # this is just to make the console read clearer
    a_sqr = a ** 2
    b_sqr = b ** 2
    sum_a_b = a_sqr + b_sqr
    print('the sum of a squared plus b squared is', sum_a_b)
    return 0

# refactor the code to remove the print statements and return the square root of a^2 and b^2
def hyp_step4(a, b):
    a_sqr = a ** 2
    b_sqr = b ** 2
    sum_a_b = a_sqr + b_sqr
    return math.sqrt(sum_a_b)


def display_hypo(a, b):
    print('The hypotenuse of a triangle with the side a:{a} and side b:{b} is:{c}'.format(a=a, b=b, c=hyp_step4(a, b)))

def main():
    a = 3
    b = 4
    print("return of step 1 ->", hyp_step1(a, b))
    print("return of step 2 ->", hyp_step2(a, b))
    print("return of step 3 ->", hyp_step3(a, b))
    print("return of step 4 ->", hyp_step4(a, b))
    a2 = 5
    b2 = 8
    display_hypo(a2, b2)
    a3 = 7
    b3 = 5
    display_hypo(a3, b3)


main()
