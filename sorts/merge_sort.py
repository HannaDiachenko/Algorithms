def merge_sort(data):
    left_data = (data[:len(data) // 2])
    right_data = (data[len(data) // 2:])
    sort_data = []
    if len(data) <= 1:
        return data
    sort_left_data = merge_sort(left_data)
    sort_right_data = merge_sort(right_data)
    while len(sort_left_data) != 0 or len(sort_right_data) != 0:
        if len(sort_left_data) == 0 and len(sort_right_data) != 0:
            sort_data.append(sort_right_data[0])
            sort_right_data.remove(sort_right_data[0])
        elif len(sort_left_data) != 0 and len(sort_right_data) == 0:
            sort_data.append(sort_left_data[0])
            sort_left_data.remove(sort_left_data[0])
        else:
            if sort_left_data[0] <= sort_right_data[0]:
                sort_data.append(sort_left_data[0])
                sort_left_data.remove(sort_left_data[0])
            else:
                sort_data.append(sort_right_data[0])
                sort_right_data.remove(sort_right_data[0])

    return sort_data
