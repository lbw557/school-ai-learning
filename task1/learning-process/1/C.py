import asyncio
import time

async def task1():
    start = time.time()
    await asyncio.sleep(1)
    end = time.time()
    return end - start

async def task2():
    start = time.time()
    await asyncio.sleep(2)
    end = time.time()
    return end - start

async def task3():
    start = time.time()
    await asyncio.sleep(3)
    end = time.time()
    return end - start

async def main():
    start = time.time()
    result=await asyncio.gather(task1(), task2(), task3())
    end = time.time()
    print(result)
    print(end-start)

asyncio.run(main())

#async def 定义的函数，调用时是否会立即执行函数体？
#await 是否意味着阻塞整个线程？
#asyncio.gather() 与 asyncio.create_task() 有什么区别？
#如果在协程里使用 time.sleep(3)，会对其他协程造成什么影响？

#1.不会
#2.不会，只会阻塞当前任务或协程
#asyncio.gather()可以同时执行多个任务并按照输入顺序输出结果；asyncio.create_task()仅为创建任务和运行任务
#会直接堵塞所有协程