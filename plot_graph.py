import random
import matplotlib.pyplot as plt
from matplotlib import animation
from sorting.Data import Data
from sorting.selection_sort import selection_sort
from sorting.bubble_sort import bubble_sort
from sorting.insertion_sort import insertion_sort
from sorting.merge_sort import merge_sort
from sorting.quick_sort import quick_sort


s_type = {
    1: 'Selection Sort',
    2: 'Bubble Sort',
    3: 'Insertion Sort',
    4: 'Merge Sort',
    5: 'Quick Sort'
}


def draw_chart(sort_type, original_data, frame_interval):
    fig = plt.figure(1, figsize=(16, 9))
    data_set = [Data(d) for d in original_data]
    axs = fig.add_subplot(111)
    plt.subplots_adjust(left=0.01, bottom=0.01, right=0.99, top=0.95)

    if sort_type == 1:
        frames = selection_sort(data_set)
    elif sort_type == 2:
        frames = bubble_sort(data_set)
    elif sort_type == 3:
        frames = insertion_sort(data_set)
    elif sort_type == 4:
        frames = merge_sort(data_set)
    elif sort_type == 5:
        frames = quick_sort(data_set)
    else:
        raise IndexError

    def animate(frame_no):
        # if fi % 2 != 0 and frame_interval < 10 and fi != len(frames)-1:
        #     return
        bars = []
        if len(frames) > frame_no:
            axs.cla()
            axs.set_title(s_type[sort_type])
            axs.set_xticks([])
            axs.set_yticks([])
            bars += axs.bar(list(range(Data.length)),
                            [d.value for d in frames[frame_no]],
                            1,
                            color=[d.color for d in frames[frame_no]]
                            ).get_children()
        frame_no += 1
        return bars

    anim = animation.FuncAnimation(fig, animate, frames=len(frames), interval=frame_interval, repeat=False)
    return plt, anim


data_type = input("Input Data(i) or Generate Randomly(r) (i/r): ")
if data_type.lower() == 'r':
    length = 300
    try:
        length = int(input("Length of the data (max. 200): "))
    except ValueError:
        print("Length must be an integer")
    if length > 200:
        raise Exception("Length must be less than 200")
    Data.length = length
    data = list(range(1, length+1))
    random.shuffle(data)
elif data_type.lower() == 'i':
    data = list(map(int, input("Enter the data with space in between (E.g. 1 2 3 4): ").split()))
    Data.length = len(data)
else:
    raise ValueError("Input must be 'i' or 'r'")

print("Please select sorting type")
print("1. Selection Sort")
print("2. Bubble Sort")
print("3. Insertion Sort")
print("4. Merge Sort")
print("5. Quick Sort")
sort_type = 6
try:
    sort_type = int(input("Please select from above list: "))
except:
    raise ValueError("Input must be an integer")
frame_speed = 10
try:
    frame_speed = int(input("Please specify frame speed (default: 10): ") or frame_speed)
except ValueError:
    raise ValueError("Frame Speed must be integer")
if frame_speed <= 0:
    raise Exception("Frame speed must be positive")
if 1 <= sort_type <= 5:
    plt, _ = draw_chart(sort_type, data, frame_speed)
    plt.show()
else:
    raise Exception("Input must be only from above list")