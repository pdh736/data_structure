def print_recursive(ary):
    for value in ary :
        if type(value) is list:
            print_recursive(value)
        else:
            print(value)

a = [1,2,3,[4,5,6],7,8,9]

print_recursive(a)
