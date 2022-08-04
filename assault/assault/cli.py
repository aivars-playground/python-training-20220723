import json
from typing import TextIO
from unittest import result
import click

from assault.stats import Results
from .connector import assault


@click.command()
@click.option("--requests", "-r", default=500, help="NR of requests")
@click.option("--concurrency", "-c", default=1, help="NR of concurrent requests")
@click.option("--json-file", "-j", default=None, help="output json file")
@click.argument("url")
def cli(requests, concurrency, json_file, url):
    total_time, request_dict = assault(url, requests, concurrency)
    result = Results(total_time, request_dict)
    output_file = open(json_file, "w")
    display(result, output_file)


def display(result: Results, output_file: TextIO):
    if output_file:
        with output_file:
            json.dump(
                {
                    "successful_requests": result.successful_requests(),
                    "slowest": result.slowest(),
                    "Fastest": result.fastest(),
                },
                output_file,
            )
    else:
        print("print to screen")
        print(f"Successful {result.successful_requests()}")
        print(f"Slowest {result.slowest()}")
        print(f"Fastest {result.fastest()}")
        print(f"Average {result.average_time()}")
        print(f"Total {result.total_time}")
        print(f"Req/min {result.requests_per_minute()}")
        print(f"Req/sec {result.requests_per_second()}")


if __name__ == "__main__":
    cli()
