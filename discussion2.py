# name in the function definition is a parameter
def welcome(name):
    print(f'Welcome to the world of python Mr./Mrs. {name}')


def format_name(name):
    return name.title()


def local_variable_function(my_arg):
    local_var = 10
    return local_var + my_arg


local_var = 12

if __name__ == '__main__':
    # "John" is an argument as it is passed to the function
    print("this is argument was a value")
    welcome("John")
    my_name = "Johnny"
    print("this is argument was a variable")
    welcome(my_name)
    print("this is argument was a function with a value passed to it as an argument")
    welcome(format_name("john"))
    print("calling a function that contains a local variable")
    x = local_variable_function(14)
    print(x)
    # or call as
    print(local_variable_function(45))
    # trying to call a local variable outside of its scope creates an undefined variable ref unless the variable is
    # also declared outside the function in which case it shadows the local variable does not change the output of
    # the function call as it will use the local variable
    print(local_var)
