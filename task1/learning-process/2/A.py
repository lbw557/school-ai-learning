import asyncio
import httpx

async def fetch():
    async with httpx.AsyncClient() as client:
        response=await client.get("https://jsonplaceholder.typicode.com/users/1")
        print(response.status_code)
        print(response.json())

async def main():
    await fetch()

asyncio.run(main())
