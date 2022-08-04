import click


@click.command()
@click.option("--requests", "-r", default=500, help="NR of requests")
@click.option("--concurrency", "-c", default=1, help="NR of concurrent requests")
@click.option("--json-file", "-j", default=None, help="output json file")
@click.argument("url")
def cli(requests, concurrency, json_file, url):
    print(f"Req:{requests}, con:{concurrency}, json:{json_file}, url:{url}")
    pass


if __name__ == "__main__":
    cli()
