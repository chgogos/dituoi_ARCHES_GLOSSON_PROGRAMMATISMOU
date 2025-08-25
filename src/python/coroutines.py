import asyncio
import random

async def task1():
    delay = random.randint(3, 10)
    print(f"Task 1 started (sleeping for {delay} seconds)")
    await asyncio.sleep(delay)
    print(f"Task 1 finished after {delay} seconds")

async def task2():
    delay = random.randint(3, 10)
    print(f"Task 2 started (sleeping for {delay} seconds)")
    await asyncio.sleep(delay)
    print(f"Task 2 finished after {delay} seconds")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())
