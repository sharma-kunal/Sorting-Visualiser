from sorting.Data import Data
from copy import deepcopy


def insertion_sort(data):
    frames = [data]
    new_data = deepcopy(data)
    for i in range(1, Data.length):
        for k in range(i):
            new_data[k].set_color('pink')
        frames.append(deepcopy(new_data))
        frames[-1][i].set_color('r')
        for j in range(i, 0, -1):
            if new_data[j].value < new_data[j-1].value:
                new_data[j], new_data[j-1] = new_data[j-1], new_data[j]
                frames.append(deepcopy(new_data))
                frames[-1][j-1].set_color('r')
            else:
                break
    for i in range(Data.length):
        new_data[i].set_color('pink')
    frames.append(new_data)
    return frames
