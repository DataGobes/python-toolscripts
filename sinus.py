#modules
import numpy as np
import matplotlib.pyplot as plt

sta = int(input('Where to start plotting ?:'))
sto = int(input('Where to stop plotting? :'))

plt.plot([np.sin(x) for x in np.arange(start=sta, stop=sto, step=0.01)], label='sinus')
plt.plot([np.cos(x) for x in np.arange(start=sta, stop=sto, step=0.01)], label='cosinus')
plt.xlabel('0.01 increments')
plt.ylabel('value')
plt.legend()
plt.show()
