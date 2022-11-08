import numpy as np
import matplotlib.pyplot as plt

pi = int()
n = int()


def monte_carlo():
    global pi
    
    n_in = 0  # 円の中に入った乱数の個数の初期値
    x1 = np.random.rand(n, 2)

    # モンテカルロ法
    for i in range(n):
        if (x1[i, 0]**2+x1[i, 1]**2)**0.5 < 1:  # 半径1の円の内側に入る場合
            n_in = n_in+1
    pi = 4*(n_in/n)
