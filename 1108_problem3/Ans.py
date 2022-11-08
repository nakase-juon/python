import numpy as np
import matplotlib.pyplot as plt
from statistics import stdev

pi = int()
n = int()


def monte_carlo():
    global pi
    global n
    
    n_in = 0  # 円の中に入った乱数の個数の初期値
    x1 = np.random.rand(n, 2)

    # モンテカルロ法
    for i in range(n):
        if (x1[i, 0]**2+x1[i, 1]**2)**0.5 < 1:  # 半径1の円の内側に入る場合
            n_in = n_in+1
    pi = 4*(n_in/n)


def meanAndStdev():
    global pi
    global n
    
    pi_list = list()  # N回の試行結果を格納するリスト
    mean_list = list()
    stdev_list = list()

    n = 100
    plt.figure(figsize=(5, 5))

    while n <= 10000:
        monte_carlo()
        pi_list.append(pi)
        if(len(pi_list) > 1):
            mean_list.append(sum(pi_list)/len(pi_list))
            stdev_list.append(stdev(pi_list))
        n += 200

    x = [x for x in range(200, 10000, 200)]

    plt.xlabel('number of points')
    plt.ylabel('average of obtained π')
    plt.xlim(-500, 10500)
    plt.ylim(2.97, 3.28)
    plt.grid()
    plt.errorbar(x, mean_list , yerr=stdev_list, color='red', fmt='o', capsize=3)
    plt.plot(x, mean_list, color='red')

    plt.show()

if __name__ == '__main__':
    meanAndStdev()
