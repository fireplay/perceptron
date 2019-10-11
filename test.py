import numpy as np
from matplotlib import pyplot as plt


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

######################################################################

x = np.arange(-3, 3, 0.5)
y = 2*x

ax.plot(x, y, 'g-')

plt.show()