
#quick sort1
def quick(ary):
    if len(ary) <= 1:
        return ary

    pivot = ary[-1]

    low = []
    high = []

    for v in ary[:-1]:
        if pivot >= v:
            low.append(v)
        else :
            high.append(v)

    low = quick(low)
    high = quick(high)

    result = low
    result += [pivot]
    result += high

    return result



def quick2(ary, left_idx, right_idx):
    if right_idx - left_idx <= 0:
        return

    right = right_idx 
    left = left_idx
    pivot_idx = right_idx

    while left < right:
        while ary[left] < ary[pivot_idx] and left < right_idx:
            left += 1
        while ary[right] >= ary[pivot_idx] and right > left_idx:
            right -= 1

        if left < right :
            ary[left], ary[right] = ary[right], ary[left]
        else :
            ary[left], ary[right_idx] = ary[right_idx], ary[left]

    quick2(ary, left_idx, left-1)
    quick2(ary, left+1, right_idx)

ary = [7, 1, 4, 2, 3]
quick2(ary, 0, len(ary)-1)
print(ary)
