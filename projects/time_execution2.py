from timeit import default_timer

import time 
import random


def be_busy():
    sleep_time = random.uniform(1, 3)
    time.sleep(sleep_time)


start_time = default_timer()
be_busy()
end_time = default_timer()

elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time} seconds")
