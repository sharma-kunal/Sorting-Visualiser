from sorting.Data import Data
from copy import deepcopy


def selection_sort(data):
    frames = [data]
    new_data = deepcopy(data)
    for i in range(0, Data.length - 1):
        min_idx = i
        for j in range(i + 1, Data.length):
            updated_data = deepcopy(new_data)
            updated_data[i].set_color('k')
            updated_data[j].set_color('r')
            frames.append(updated_data)
            if new_data[min_idx].value > new_data[j].value:
                min_idx = j
        new_data[i], new_data[min_idx] = new_data[min_idx], new_data[i]
        new_data[i].set_color('pink')
    new_data[-1].set_color('pink')
    frames.append(new_data)
    return frames