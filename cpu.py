import time
import psutil
import numpy as np

while True:
    a = psutil.cpu_percent(percpu=True)
    print('CPU percentages :'+str(a) + ' Mean :' + str(np.around(np.mean(a),decimals=2)))
    time.sleep(1)