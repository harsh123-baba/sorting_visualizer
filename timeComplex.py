import time;
from Algorithms.quickSort import quickSort
from random import randint


list1 = [randint(0,1000) for i in range(20000)]
times = [];

for x in range(0,20001,100):
    start_time = time.time()
    list2 = quickSort(list1[:x], 0, x-1)
    elapsed_time = time.time() - start_time
    times.append(elapsed_time)

print(times);
x=[i for i in range(0,20001,100)]


import matplotlib.pyplot as plt

plt.xlabel("No. of elements")
plt.ylabel("Time required")
plt.plot(x,times)
