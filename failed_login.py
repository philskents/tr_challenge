from pprint import pprint
import socket
import typer
from splunklib.client import connect
import splunklib.results as results


def display(response):
    reader = results.ResultsReader(response)
    typer.secho("---- Failed Logins ---", fg=typer.colors.MAGENTA)
    for result in reader:
        if isinstance(result, dict):
            login = ("timestamp={2} user={0} src=:{1}").format(result["user"],result["src"],result["timestamp"])
            typer.echo(login)

def main(host: str = typer.Option(..., prompt=True, help="Splunk hostname"),
        port: int = typer.Option(8089,help="Splunk REST API port"),
        username: str = typer.Option(..., prompt=True, help="Splunk username"),
        password: str = typer.Option(..., prompt=True, hide_input=True, help="Splunk password")):

    search = """search index=_audit action="login attempt" info="failed" earliest=-7d@d | table timestamp user src"""
    service = connect(host=host, port=port, username=username, password=password)
    socket.setdefaulttimeout(None)
    response = service.jobs.oneshot(search)

    display(response)

if __name__ == "__main__":
    typer.run(main)
