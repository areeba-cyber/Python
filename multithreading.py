# The first use of multi-threading is that when you want to download resourses parallelly
# Done by multi-threading module
import threading
import time

def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

# time1 = time.perf_counter()
# Normal Code
# func(4)
# func(2)
# func(1)
# time2 = time.perf_counter()
# print(time2-time1)

# Code using thread
time1 = time.perf_counter()
t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[2])
t3 = threading.Thread(target=func, args=[1])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

time2 = time.perf_counter()
print(time2-time1)