import asyncio
import httpx
import time

def fetch1(client, url):
    response = client.get(url)
    return response.status_code,response.json()

async def fetch2(client, url):
    response =await client.get(url)
    return response.status_code,response.json()

def main1():
    start = time.time()
    url = ["https://jsonplaceholder.typicode.com/users/1",
           "https://jsonplaceholder.typicode.com/users/2",
           "https://jsonplaceholder.typicode.com/users/3"]
    with httpx.Client() as client:
        response=[]
        for url in url:
            response.append(fetch1(client,url))
    print(response)
    print("串行：",time.time() - start,"second")

async def main2():
    start = time.time()
    url = ["https://jsonplaceholder.typicode.com/users/1",
           "https://jsonplaceholder.typicode.com/users/2",
           "https://jsonplaceholder.typicode.com/users/3"]
    async with httpx.AsyncClient() as client:
        tasks=[]
        for url in url:
            tasks.append(fetch2(client,url))
        response=await asyncio.gather(*tasks)
    print(response)
    print("并行：",time.time() - start,"second")

main1()
asyncio.run(main2())

#为什么推荐多个 HTTP 请求共用一个 AsyncClient？
#await client.get() 等待服务器响应期间，事件循环可以做什么？
#async with 和普通 with 有什么区别？
#三个 HTTP 请求并发执行，为什么不一定严格比串行快 3 倍？

#1.能减少新建客户端导致的资源消耗
#2.可以get其他url的信息或者执行其他task
#3.async with可以执行异步请求，with只能执行并步
#4.因为还有服务器延迟，网络堵塞，多tcp处理等其他因素

#纠正：with 和 async with 的区别，不是一个负责异步请求，一个负责同步请求。它们真正的区别是：两者使用不同的上下文管理协议。
#一个是同步上下文管理器，另一个是异步上下文管理器