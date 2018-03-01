def bubble_sort(data, key=None):
    if key is None:
        key = lambda x: x

    for index in range(len(data) - 1):
        for i in range(len(data) - 1):
            if key(data[i]) > key(data[i + 1]):
                memory_element = data[i]
                data[i] = data[i + 1]
                data[i + 1] = memory_element

    return data
