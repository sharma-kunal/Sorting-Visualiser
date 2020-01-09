from sorting.Data import Data
from copy import deepcopy


def bubble_sort(data):
    frames = [data]
    new_data = deepcopy(data)
    for i in range(Data.length):
        for j in range(0, Data.length-i-1):
            updated_data = deepcopy(new_data)
            updated_data[j].set_color('r')
            updated_data[j+1].set_color('k')
            frames.append(updated_data)
            if new_data[j].value > new_data[j+1].value:
                new_data[j].value, new_data[j+1].value = new_data[j+1].value, new_data[j].value
        new_data[Data.length-i-1].set_color('pink')
    frames.append(new_data)
    return frames