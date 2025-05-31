

import matplotlib.pyplot as plt
import numpy as np

x1 = ['0.1', '0.3', '0.5', '0.7', '0.9']
x2 = ['0.1', '0.3', '0.5', '0.7', '0.9']
x3 = ['0.1', '0.3', '0.5', '0.7', '0.9']
x5 = ['0.1', '0.3', '0.5', '0.7', '0.9']

y1 = [57.6, 59.4, 60.7, 61.9, 60.9]
y2 = [38.3, 39.5, 38.8, 43.5, 38.6 ]
y3 = [27.3, 29.9, 29.0, 32.4, 26.2 ]
y5 = [31.9, 34.0, 33.2, 37.1, 31.2 ]

plt.figure(figsize=(10, 7))
font1 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 34}
plt.rc('font', **font1)
plt.plot(x1, y1, label='AUC', linewidth=5, color='#1f77b4', marker='o', markerfacecolor='#1f77b4', markersize=14)
plt.plot(x2, y2, label='Pre', linewidth=5, color='#ff7f0e', marker='s', markerfacecolor='#ff7f0e', markersize=14)
plt.plot(x3, y3, label='Rec', linewidth=5, color='#2ca02c', marker='D', markerfacecolor='#2ca02c', markersize=14)
plt.plot(x5, y5, label='MCC', linewidth=5, color='#9467bd', marker='^', markerfacecolor='#9467bd', markersize=14)
y_min = 30
y_max = 80
plt.yticks(np.arange(y_min - 5, y_max + 5, 10))
ax = plt.gca()
ax.spines['bottom'].set_linewidth(5)
ax.spines['top'].set_linewidth(5)
ax.spines['right'].set_linewidth(5)
ax.spines['left'].set_linewidth(5)
plt.savefig('2.pdf', dpi=600, bbox_inches='tight')
plt.show()