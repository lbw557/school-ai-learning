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
    url = [
        "https://httpbin.org/delay/1?id=1",
        "https://httpbin.org/delay/1?id=2",
        "https://httpbin.org/delay/1?id=3"
    ]
    with httpx.Client() as client:
        response=[]
        for url in url:
            response.append(fetch1(client,url))
    print(response)
    print("串行：",time.time() - start,"second")

async def main2():
    start = time.time()
    url = [
        "https://httpbin.org/delay/1?id=1",
        "https://httpbin.org/delay/1?id=2",
        "https://httpbin.org/delay/1?id=3"
    ]
    async with httpx.AsyncClient() as client:
        tasks=[]
        for url in url:
            tasks.append(fetch2(client,url))
        response=await asyncio.gather(*tasks)
    print(response)
    print("并行：",time.time() - start,"second")

main1()
asyncio.run(main2())