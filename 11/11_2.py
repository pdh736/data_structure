
def even_collector(num_list):
    dst_list = list()

    if len(num_list) == 0:
        return []

    if num_list[0] % 2 == 0:
        dst_list.append(num_list[0])

    return dst_list + even_collector(num_list[1:])


print(even_collector([10, 7, 8]))
