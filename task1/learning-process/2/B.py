import asyncio
import httpx

async def fetch(client, url):
    response = await client.get(url)
    return response.status_code,response.json()

async def main():
    url = ["https://jsonplaceholder.typicode.com/users/1",
           "https://jsonplaceholder.typicode.com/users/2",
           "https://jsonplaceholder.typicode.com/users/3"]
    async with httpx.AsyncClient() as client:
        tasks = []
        for url in url:
            tasks.append(fetch(client,url))
        results = await asyncio.gather(*tasks)
        print(results)

asyncio.run(main())