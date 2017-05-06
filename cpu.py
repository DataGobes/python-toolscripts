import time
import psutil

while True:
    print(psutil.cpu_percent(percpu=True))
    time.sleep(1)