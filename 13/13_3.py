

def find_max1(ary):
    for v1 in ary:
        is_max = True
        for v2 in ary:
            if v2 > v1:
                is_max = False

        if is_max :
            return v1


def find_max2(ary):
    ary.sort()
    return ary[-1]


def find_max3(ary):
    max_num = 0

    for v in ary:
        if v > max_num:
            max_num = v

    return max_num



ary = [5, 7, 8, 3, 10]

print(find_max1(ary))
print(find_max2(ary))
print(find_max3(ary))
