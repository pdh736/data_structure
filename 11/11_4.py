

def get_x_pos(str) :
    if len(str) == 0:
        return 10;
    if str[0] == 'x':
        return 0;
    return 1 + get_x_pos(str[1:])


print(get_x_pos('abcdefghijklmnopqrstuvwxyz'))
print(get_x_pos('abcxd'))
