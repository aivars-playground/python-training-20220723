import sys
import json
import click
from .http import ping_servers


@click.command()
@click.option("--filename", "-f", default=None)
@click.option("--server", "-s", default=None)
def cli(filename, server):
    """cli entry"""
    if not (filename or server):
        raise click.UsageError("missing filename or server")

    # unique collection of servers to be checked
    servers = set()

    if filename:
        try:
            with open(filename, encoding="UTF8") as file:
                json_servers = json.load(file)
                for json_server in json_servers:
                    servers.add(json_server)
        except Exception as ex:
            print("Error: Unable to read JSON", ex)
            sys.exit(1)

    if server:
        servers.add(server)

    print(f"calling:{servers}")
    print(ping_servers(servers))
