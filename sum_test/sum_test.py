from __future__ import division

import time
import numpy as np
from matplotlib import pyplot as plt

repeat = 1000
array_size = 30
array = np.random.random(array_size)

result_manual = np.empty(array_size)
result_sum = np.empty(array_size)

for sum_size in range(array_size):
    print(sum_size)
    # Manuel
    start = time.time()
    for _ in range(repeat):
        sum_ = 0
        for n in range(sum_size):
            sum_ += array[n]
    result_manual[sum_size] = (time.time() - start) / repeat

    # Sum
    start = time.time()
    for _ in range(repeat):
        sum_ = array[:sum_size].sum()
    result_sum[sum_size] = (time.time() - start) / repeat

sizes = list(range(array_size))
plt.plot(sizes, result_manual, label='manual')
plt.plot(sizes, result_sum, label='sum')
plt.legend()
plt.yscale('log')
plt.show()
