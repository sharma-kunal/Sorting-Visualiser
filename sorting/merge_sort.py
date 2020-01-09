import copy
from sorting.Data import Data


def merge_sort(data):
    frames = [data]
    new_data = copy.deepcopy(data)
    merge(new_data, 0, Data.length, frames)
    frames.append(new_data)
    return frames


def merge(data, start, end, frames):
    mid = (start + end) // 2
    if end - start > 2:
        merge(data, start, mid, frames)
        merge(data, mid, end, frames)
    updated_data = copy.deepcopy(data)
    # Merge.
    left = start
    right = mid
    tmp = []
    for i in range(start, end):
        # FRAME OPERATION BEGIN
        frames.append(copy.deepcopy(updated_data))
        # FRAME OPERATION END
        try:
            frames[-1][left].set_color('r')
            frames[-1][right].set_color('b')
        except IndexError:
            pass
        if right == end or (left < mid and data[left].value <= data[right].value):
            tmp.append(data[left])
            left += 1
        else:
            tmp.append(data[right])
            right += 1
    for i in range(start, end):
        data[i] = tmp[i-start]
        data[i].set_color('pink')
    frames.append(copy.deepcopy(data))