import numpy as np
import matplotlib.pyplot as plt

start = int(input('Where to start plotting ?:'))
stop = int(input('Where to stop plotting? :'))

plt.plot([np.sin(x) for x in np.arange(start=start, stop=stop, step=0.01)], label='sinus')
plt.plot([np.cos(x) for x in np.arange(start=start, stop=stop, step=0.01)], label='cosinus')
plt.xlabel('0.01 increments')
plt.ylabel('value')
plt.legend()
plt.show()
