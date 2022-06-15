

def find_missing_number(ary):
    ary.sort()

    for i in range(0, len(ary)):
        if i != ary[i]:
            return i

    return -1


ary = [5, 2, 4, 1, 0]


print(find_missing_number(ary))

        
