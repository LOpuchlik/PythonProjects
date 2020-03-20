import matplotlib.pyplot as plt; plt.rcdefaults()
import time
import numpy as np
import random


def bubblesort(size=100):
    lower_bound=5
    upper_bound=1000
    def generate_array():
        arr = []
        for i in range(size):
            arr.append(random.randint(lower_bound, upper_bound))
        return arr

    unsorted = generate_array()
    sorted_arr = sorted(unsorted)

    if unsorted != sorted_arr:
        for num in range(len(unsorted)-1,0,-1):
            for i in range(num):
                time.sleep(0.005)
                plt.bar(np.arange(len(unsorted)), unsorted, align='center', alpha=0.5)
                plt.xticks(None)
                plt.show()
                time.sleep(0.005)
                if unsorted[i]>unsorted[i+1]:
                    temp = unsorted[i]
                    unsorted[i] = unsorted[i+1]
                    unsorted[i+1] = temp
    else:
        return unsorted


bubblesort(10)
