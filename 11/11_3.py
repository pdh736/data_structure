
def triangular(num):
    if num == 1:
        return 1
    return num + triangular(num -1) 

print(triangular(7))
