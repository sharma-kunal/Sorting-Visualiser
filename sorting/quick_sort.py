from sorting.Data import Data
from copy import deepcopy


def quick_sort(data):
    frames = [data]
    new_data = deepcopy(data)
    quick(new_data, 0, Data.length-1, frames)
    frames.append(new_data)
    return frames


def quick(data, start, end, frames):
    if start < end:
        new_data = deepcopy(data)
        i = start
        j = end
        pivot = new_data[j].value
        new_data[j].set_color('k')
        for k in range(i, j):
            new_data[k].set_color('r')
            if data[k].value < pivot:
                data[i].value, data[k].value = data[k].value, data[i].value
                i += 1
            frames.append(new_data)
            new_data = deepcopy(data)
            new_data[j].set_color('k')
        data[i], data[end] = data[end], data[i]
        data[i].set_color('pink')
        quick(data, start, i-1, frames)
        quick(data, i+1, end, frames)
    elif start == end:
        data[start].set_color('pink')
