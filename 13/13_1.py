

def max_mul(ary):
    ary.sort()

    return ary[-1]*ary[-2]*ary[-3]


ary = [5, 6, 1, 8]
print(max_mul(ary))
