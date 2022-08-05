"""making async http requests"""
import os
from dataclasses import dataclass
import asyncio
import requests

DEBUG = os.getenv("DEBUG")


def ping_servers(servers):
    """initialize async task"""
    results = {"success": [], "failures": []}
    asyncio.run(make_requests(servers, results))
    return results


async def make_requests(servers, results):
    """co-routine to distribute work"""
    tasks = [asyncio.create_task(ping(server, results)) for server in servers]
    await asyncio.gather(*tasks)  # unpack


async def ping(server, results):
    """task to make request"""
    # requests do not support asyncio, wrapping result in future
    loop = asyncio.get_event_loop()
    future_result = loop.run_in_executor(None, get_response, server)
    result = await future_result
    if result.status_code in range(200, 299):
        results["success"].append(server)
    else:
        results["failures"].append(server)


def get_response(server):
    """makes request"""
    try:
        if DEBUG:
            print(f"requesting:{server}", DEBUG)
        response = requests.get(server)
        if DEBUG:
            print(f"got:{response}")
        return response
    except Exception as ex:
        if DEBUG:
            print(f"error:{server}", ex)
        return FakeResponse(-1, server)


@dataclass
class FakeResponse:
    """Fake response to a HTTP request"""

    status_code: int
    server: str


# calling module as script
if __name__ == "__main__":
    print("do not call directly")
