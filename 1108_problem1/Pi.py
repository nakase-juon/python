import numpy as np
import matplotlib.pyplot as plt

pi = int()
n = int()


def monte_carlo():
    global pi
    # N = [10, 100, 1000, 10000]

    # for n in N:
    # print('Nの値を入力してください:n=', end='')
    # n = int(input())  #10,100,1000,10000のいずれかを入力する

    n_in = 0  # 円の中に入った乱数の個数の初期値
    # plt.figure(figsize=(5, 5))
    x1 = np.random.rand(n, 2)

    # モンテカルロ法
    for i in range(n):
        if (x1[i, 0]**2+x1[i, 1]**2)**0.5 < 1:  # 半径1の円の内側に入る場合
            plt.plot(x1[i, 0], x1[i, 1], color='red', marker='o', markersize=2)
            n_in = n_in+1
        else:  # 半径1の円の外側に入る場合　
            plt.plot(x1[i, 0], x1[i, 1], color='blue', marker='o', markersize=2)
    pi = 4*(n_in/n)
    print('πの予測値:4*(n_in/n)=', pi)
    # plt.xlabel("x")
    # plt.ylabel("y")
    # plt.show()

# if __name__ == '__main__':
#     monte_carlo()
