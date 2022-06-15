def add_until_100(ary) :
    if len(ary) == 0 :
        return 0

    sum = add_until_100(ary[1:])

    if ary[0] + sum >100 :
        return sum

    return ary[0] + sum

