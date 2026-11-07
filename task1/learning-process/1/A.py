import asyncio
import time

async def main():
    start = time.time()
    await taskA()
    await taskB()
    await taskC()
    end = time.time()
    print(end - start,"second")

async def taskA():
    await asyncio.sleep(1)

async def taskB():
    await asyncio.sleep(2)

async def taskC():
    await asyncio.sleep(3)

asyncio.run(main())