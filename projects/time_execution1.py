import time
import random


def be_busy():
    sleep_time = random.uniform(1, 3)
    time.sleep(sleep_time)


start_time = time.time()
be_busy()
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time} seconds")
