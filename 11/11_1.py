
def count_recur(ary) :
    if len(ary) == 1:
        return len(ary[0])

    return len(ary[0]) + count_recur(ary[1:])


str_list = ["ab", "c", "def", "ghij"]


print(count_recur(str_list))
