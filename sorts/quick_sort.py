import random

def quick_sort(data):
    left_data = []
    right_data = []
    sort_data = []

    if len(data) <= 1:
        return data

    pivot = random.choice(data)

    for i in range(len(data)):
        if data[i] < pivot:
            left_data.append(data[i])
        elif data[i] > pivot:
            right_data.append(data[i])
        else:
            sort_data.append(data[i])

    sort_left_data = quick_sort(left_data)
    sort_right_data = quick_sort(right_data)
    sort_data = sort_left_data+sort_data+sort_right_data

    return sort_data
