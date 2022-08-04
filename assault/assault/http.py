import asyncio
import time
import os
import requests


def fetch(url):
    """make request, return result"""
    started_at = time.monotonic
    response = requests.get(url)
    request_time = time.monotonic - started_at
    return {"status_code": response.status_code, "request_time": request_time}


async def worker(name, queue, results):
    """take requests from queue, do the work, put result"""
    # python is single threaded
    loop = asyncio.get_event_loop()
    while True:
        url = await queue.get()
        print(f"{name} - fetch:{url}")
        future_result = loop.run_in_executor(None, fetch, url)
        result = await future_result
        results.append(result)
        queue.task_done()


# this async  can be run by asyncio or with await...
async def distribute_work(url, requests, concurrency, results):
    """divide work in batches, collect results"""
    queue = asyncio.Queue()

    for _ in range(requests):  # do not care about actual number
        queue.put_nowait(url)

    tasks = []
    for i in range(concurrency):
        task = asyncio.create_task(worker(f"worker-{i+1}", queue, results))
        tasks.append(task)

    # statistics
    started_at = time.monotonic
    await queue.join()  # wait till everything finishes
    total_time = time.monotonic - started_at

    for task in tasks:
        task.cancel()  # task has to be stopped explicitly

    print(f"took total time: {total_time:.2f}, to execute {requests} requests")


def assault(url, requests, concurrency):
    """entry point to make requests"""
    results = []
    asyncio.run(distribute_work(url, requests, concurrency, results))
    print(results)


if __name__ == "__main__":
    assault("https://google.com", 1, 1)
