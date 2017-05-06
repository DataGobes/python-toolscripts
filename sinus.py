import numpy as np
import matplotlib.pyplot as plt

plt.plot([np.sin(x) for x in np.arange(start=-5, stop=5, step=0.01)], label='sinus')
plt.plot([np.cos(x) for x in np.arange(start=-5, stop=5, step=0.01)], label='cosinus')
plt.legend()
plt.show()
