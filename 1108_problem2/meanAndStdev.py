import numpy as np
import matplotlib.pyplot as plt
from statistics import stdev

import Pi as p

pi_list = list()
mean_list = list()
stdev_list = list()

p.n = 100
plt.figure(figsize=(10, 5))
while p.n <= 10000:
    p.monte_carlo()
    pi_list.append(p.pi)
    if(len(pi_list) > 1):
        mean_list.append(sum(pi_list)/len(pi_list))
        stdev_list.append(stdev(pi_list))
    p.n += 200

x = [x for x in range(200, 10000, 200)]

plt.subplot(121)
plt.xlabel('number of points')
plt.ylabel('average of obtained π')
plt.xlim(-500, 10500)
plt.grid()
plt.plot(x, mean_list, color='red')

plt.subplot(122)
plt.xlabel('number of points')
plt.ylabel('standard deviation of obtained π')
plt.xlim(-500, 10500)
plt.grid()
plt.plot(x, stdev_list, color='red')

plt.tight_layout()
plt.show()
