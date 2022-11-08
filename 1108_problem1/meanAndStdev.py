import numpy as np
import matplotlib.pyplot as plt
from statistics import stdev

import Pi as p

pi_list = list()  # 100回の試行結果を格納するリスト
p.n = int(input())  # 10,100,1000,10000のいずれかを入力する
for num in range(100):
    p.monte_carlo()
    pi_list.append(p.pi)
print('N=' + str(p.n))
print('平均値:', sum(pi_list)/len(pi_list))
print('標準偏差:', stdev(pi_list))
