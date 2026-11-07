import asyncio
import httpx

async def fetch(client, url,sem):
    async with sem:
        response = await client.get(url)
        return response.status_code,response.json()

async def main():
    sem = asyncio.Semaphore(3)
    url = ["https://jsonplaceholder.typicode.com/users/1",
           "https://jsonplaceholder.typicode.com/users/2",
           "https://jsonplaceholder.typicode.com/users/3"]
    async with httpx.AsyncClient() as client:
        tasks = []
        for url in url:
            tasks.append(fetch(client,url,sem))
            results = await asyncio.gather(*tasks,return_exceptions=True)
        for i in results:
            if isinstance(i,httpx.HTTPStatusError):
                print("HTTP状态错误")
                print("状态码:", i.response.status_code)
        print(results)

asyncio.run(main())