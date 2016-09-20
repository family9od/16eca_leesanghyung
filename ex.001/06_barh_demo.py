# -*- coding: utf8 -*-
"""
simple demo of a horizontal bar chart
간단한 수평 막대 그래프 예제
"""

import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np

people = ('tom', 'duck', 'harry', 'slim', 'kim')
y_pos = np.arange(len(people))

performance = 3 + 10 * np.random.rand(len(people))

error = np.random.rand(len(people))
plt.barh(y_pos, performance, xerr=error, align='center', alpha=0.4)
plt.yticks(y_pos, people)
plt.xlabel('performance')
plt.title('how fast do you want to go today?')
plt.show()
