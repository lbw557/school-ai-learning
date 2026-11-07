import asyncio
import json
import httpx
import os
from dotenv import load_dotenv
import argparse


async def fetch(client:httpx.AsyncClient, url:str,sem:asyncio.Semaphore)->tuple:
    async with sem:
        response = await client.get(url)
        response.raise_for_status()
        return response.status_code,response.json()

async def output()->dict:
    sem,timeout=parse_args()
    urls = ["https://jsonplaceholder.typicode.com/users/1",
           "https://jsonplaceholder.typicode.com/users/2",
           "https://jsonplaceholder.typicode.com/users/3"]
    total=len(urls)
    failed=0
    results=[]
    final={}
    async with httpx.AsyncClient(timeout=timeout) as client:
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
    return final

def json_dump(final)->None:
    with open("results.json","w") as f:
        json.dump(final,f,indent=4)

def parse_args()->tuple:
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--max_concurrency",
        type=int,
        default=int(os.getenv("MAX_CONCURRENCY","3")),
        help="最大并发请求数量"
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=int(os.getenv("REQUEST_TIMEOUT","10")),
        help="超时时间"
    )
    args = parser.parse_args()
    sem = asyncio.Semaphore(args.max_concurrency)
    timeout = args.timeout
    return sem,timeout