import matplotlib.pyplot as plt
import numpy as np
# cls_num = np.loadtxt('iNat18_class_num.txt')
# print(cls_num.shape)
label = ['w/o padding', 'w/ padding']
x = [0, 1]
y = [137235, 150930]
axes = plt.axes()
axes.set_ylim([0, 180000])

width = 0.3

plt.bar(x[0], y[0], width=width, label='w/o padding', tick_label=' ', color='#457b9d')

plt.bar(x[1], y[1], width=width, label='w/ padding', tick_label=' ', color='orange')

plt.legend(loc="upper center", fontsize=14)
# plt.xlabel('Imbalanced factor', fontsize=16)
plt.ylabel('Number of data', fontsize=16)
plt.tick_params(labelsize=12)
plt.savefig('Fig_perf_imbalanced.pdf')
plt.show()
