import numpy as np
from matplotlib import pyplot as plt

# 样本向量
X = np.array([[1, 0, 1, 1], [0, 1, 1, 1], [1, 1, 0, 1], [0, 1, 0, 1]])
# 增权向量
W = np.array([1, 1, 1, 1])
# 步长
p = 1


while True:
    flag = 0
    for i in range(np.size(X, 0)):
        res = np.dot(W, X[i])
        # w1分类，res<=0说明错了，要调整W；
        if(i == 0 or i == 1):
            if(res <= 0):
                flag = 1
                W = W + p * X[i]
                print(W)
        # w2分类，res>=0说明错了，要调整W；
        if(i == 2 or i == 3):
            if(res >= 0):
                flag = 1
                W = W - p * X[i]
                print(W)
    # 分类正确则停止，输出此时W
    if(flag == 0):
        break
