
def get_path_num(row, col, x = 0, y = 0) :
    if x == col-1 or y == row-1 :
        return 1
    return get_path_num(row, col, x+1, y) + get_path_num(row, col, x, y+1)

print(get_path_num(3, 7))
