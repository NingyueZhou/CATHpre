#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np


labels = ['Q3', 'Q8']
mmseqs = [0.820, 0.703]
hhblits = [0.824, 0.711]
nsp1 = [0.709, 0]
spider3 = [0.791, 0]
raptorx = [0.786, 0.661]
jpred4 = [0.760, 0]


x = np.arange(len(labels))
width = 0.1  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - 2*width, mmseqs, width, label='NSP2(mmseqs)')
rects2 = ax.bar(x - 1*width, hhblits, width, label='NSP2(hhblits)')
rects3 = ax.bar(x - 0*width, nsp1, width, label='NSP1')
rects4 = ax.bar(x + 1*width, spider3, width, label='Spider3')
rects5 = ax.bar(x + 2*width, raptorx, width, label='RaptorX')
rects6 = ax.bar(x + 3*width, jpred4, width, label='Jpred4')


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Accuracy')
ax.set_title('Performance of different prediction methods for CASP12 dataset')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

'''
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
ax.bar_label(rects3, padding=3)
ax.bar_label(rects4, padding=3)
ax.bar_label(rects5, padding=3)
ax.bar_label(rects6, padding=3)
'''

fig.tight_layout()

plt.show()