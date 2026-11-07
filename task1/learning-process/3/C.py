import asyncio
import json

import httpx

async def fetch(client, url,sem):
    async with sem:
        response = await client.get(url)
        response.raise_for_status()
        return response.status_code,response.json()

async def main():
    sem = asyncio.Semaphore(3)
    urls = ["https://jsonplaceholder.typicode.com/users/1",
           "https://jsonplaceholder.typicode.com/users/2",
           "https://jsonplaceholder.typicode.com/users/3"]
    total=len(urls)
    failed=0
    results=[]
    final={}
    async with httpx.AsyncClient() as client:
        tasks = []
        status = 0
        for url in urls:
            tasks.append(fetch(client,url,sem))
        result = await asyncio.gather(*tasks,return_exceptions=True)
        url_number = 0
        for i in result:
            message = {}
            if isinstance(i,httpx.HTTPStatusError) or isinstance(i,httpx.TimeoutException):
                failed+=1
                status=1
            elif isinstance(i,Exception):
                failed+=1
                status=2
            if status==0:
                message["url"]=urls[url_number]
                message["status"]="success"
                message["data"]=i[1]
            elif status==1:
                message["url"]=urls[url_number]
                message["status"]="failed"
                message["error"]=str(i)
            elif status==2:
                message["url"]=urls[url_number]
                message["status"]="failed"
                message["error"]=type(i).__name__
            results.append(message)
            status=0
            url_number += 1
    final["total"]=total
    final["success"]=total-failed
    final["failed"]=failed
    final["results"]=results
    with open("results.json","w") as f:
        json.dump(final,f,indent=4)

asyncio.run(main())

#一个 HTTP 请求失败，是否应该终止整个汇总任务？为什么？
#return_exceptions=True 会不会自动处理异常？
#asyncio.Semaphore(3) 能保证始终有三个任务运行吗？
#为什么必须分别处理请求超时、HTTP 状态错误和连接异常？

#1.不应该，因为别的请求成功了，不应该因为一个失败阻止其他的成功请求
#2.不会，只会暂存错误并继续async
#3.不能，只能保证最多有3个任务在运行
#4.因为不同报错的解决方案不同，要明白错误原因以排除错误