import numpy as np
from matplotlib import pyplot as plt
# import draw


# 样本向量
X = np.array([[-1, 4, 1], [-4, 2, 1], [2, 6, 1]])
W = np.array([1, 1, 1])
p = 1

fig = plt.figure()
ax = fig.add_subplot(111)

#####################################################################
# 将图像移到坐标原点

ax.spines['right'].set_color('none')   # 将图像右边的轴设为透明
ax.spines['top'].set_color('none')     # 将图像上面的轴设为透明
ax.xaxis.set_ticks_position('bottom')    # 将x轴刻度设在下面的坐标轴上
ax.yaxis.set_ticks_position('left')         # 将y轴刻度设在左边的坐标轴上
ax.spines['bottom'].set_position(('data', 0))   # 将两个坐标轴的位置设在数据点原点
ax.spines['left'].set_position(('data', 0))
# plt.xticks(np.arange(-6, 6))
# plt.yticks(np.arange(-6, 6))
plt.axis('equal')
######################################################################

# draw.draw_x(X)
# 画出初试的图形
for i in range(np.size(X, 0)):
    # 画X向量
    ax.plot([0, X[i][0]], [0, X[i][1]], 'b')
    # 画端点
    ax.plot(X[i][0], X[i][1], "ro")
    # 端点做标记
    ax.annotate('X[{}]'.format(i + 1), xy=(X[i][0], X[i][1]),
                xytext=(X[i][0] + 0.02, X[i][1] + 0.02))
j = 1
# draw.draw_wh(W, j)
# 画出W
ax.plot([0, W[0]], [0, W[1]], 'm')
# 画端点
ax.plot(W[0], W[1], "ro")
# 做标记
ax.annotate('W[{}]'.format(j), xy=(W[0], W[1]),
            xytext=(W[0] + 0.02, W[1] + 0.02))

# 求初始超平面H
a = np.arange(-6, 6, 0.5)
b = (-W[0] / W[1]) * a - W[2]
# 画超平面H
ax.plot(a, b, 'y-')
# 画端点
H = np.array([-6, (-W[0] / W[1]) * (-6) - W[2]])
ax.plot(H[0], H[1], "ro")
# 做标记
ax.annotate('H[{}]'.format(j), xy=(H[0], H[1]),
            xytext=(H[0] + 0.02, H[1] + 0.02))
# arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.4"))

n = 0
while n < 200:
    flag = 0
    for i in range(np.size(X, 0)):
        res = np.dot(W, X[i])
        if(res <= 0):
            flag = 1
            W = W + p * X[i]
            print(W)
            j += 1
            # draw.draw_wh(W, j)
            # 画出新的W和H
            # 画出W
            ax.plot([0, W[0]], [0, W[1]], 'm')
            # 画端点
            ax.plot(W[0], W[1], "ro")
            # 做标记
            ax.annotate('W[{}]'.format(j), xy=(W[0], W[1]),
                        xytext=(W[0] + 0.02, W[1] + 0.02))

            # 求初始超平面H
            a = np.arange(-6, 6, 0.5)
            b = (-W[0] / W[1]) * a - W[2]
            # 画超平面H
            ax.plot(a, b, 'y-')
            # 画端点
            H = np.array([-6, (-W[0] / W[1]) * (-6) - W[2]])
            ax.plot(H[0], H[1], "ro")
            # 做标记
            ax.annotate('H[{}]'.format(j), xy=(H[0], H[1]),
                        xytext=(H[0] + 0.02, H[1] + 0.02))

    if(flag == 0):
        break

plt.show()
