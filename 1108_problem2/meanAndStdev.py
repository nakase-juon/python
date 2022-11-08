import numpy as np
import matplotlib.pyplot as plt
from statistics import stdev

import Pi as p

pi_list = list()# N回の試行結果を格納するリスト
mean_list = list()
stdev_list = list()

p.n = 100
plt.figure(figsize=(10, 5))
while p.n <= 10000:
    p.monte_carlo()
    pi_list.append(p.pi)
    mean_list.append(sum(pi_list)/len(pi_list))
    if(len(pi_list) > 1):
        stdev_list.append(stdev(pi_list))
    p.n += 1

plt.subplot(121)
plt.xlabel('number of points')
plt.ylabel('average of obtained π')
plt.xlim(0, 10000)
plt.ylim(3.1, 3.17)
plt.grid()
plt.plot(mean_list, color='red')

plt.subplot(122)
plt.xlabel('number of points')
plt.ylabel('standard deviation of obtained π')
plt.xlim(0, 10000)
plt.ylim(0, 0.15)
plt.grid()
plt.plot(stdev_list, color='red')

plt.tight_layout()
plt.show()
