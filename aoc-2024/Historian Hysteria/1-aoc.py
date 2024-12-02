import numpy as np
from data import data

data = np.array(data.split())
arr_left = data[::2]
arr_right = data[1::2]
sortedL = np.array(sorted(arr_left)).astype(int)
sortedR = np.array(sorted(arr_right)).astype(int)

result = [abs(sortedL[i] - sortedR[i]) for i in range(len(sortedL))]
result2 = [i * np.count_nonzero(sortedR == i) for i in sortedL if np.count_nonzero(sortedR == i) > 0]

print("A: ", sum(result))
print("B: ", sum(result2))
