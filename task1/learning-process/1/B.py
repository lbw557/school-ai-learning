import asyncio
import time

async def task1():
    await asyncio.sleep(1)

async def task2():
    await asyncio.sleep(2)

async def task3():
    await asyncio.sleep(3)

async def main():
    start = time.time()
    await asyncio.gather(task1(), task2(), task3())
    end = time.time()
    print(end - start,"second")

asyncio.run(main())
