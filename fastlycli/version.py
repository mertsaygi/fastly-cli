from settings import *
import click
from helpers.helper import *


@click.command()
@click.option('--service', required=True)
@click.option('--version', required=True, help='version number of vcl')
@click.option('--token', envvar='FASTLY_AUTH_TOKEN')
def clone_version(token, service, version):
    headers = {'Fastly-Key': token}
    send_request("PUT", URL_FORMAT % ("/service/%s/version/%s/clone" % (service, version)), headers, None)


@click.command()
@click.option('--service', required=True, help='Fastly service name')
@click.option('--version', required=True, help='version number of vcl')
@click.option('--token', envvar='FASTLY_AUTH_TOKEN')
def activate_version(token, service, version):
    headers = {'Fastly-Key': token}
    send_request("PUT", URL_FORMAT % ("/service/%s/version/%s/activate" % (service, version)), headers, None)


@click.command()
@click.option('--service', required=True)
@click.option('--version', required=True, help='version number of vcl')
@click.option('--token', envvar='FASTLY_AUTH_TOKEN')
def get_version(token, service, version):
    headers = {'Fastly-Key': token}
    return send_request("GET", URL_FORMAT % ("/service/%s/version/%s" % (service, version)), headers,
                        None)


@click.command()
@click.option('--service', required=True)
@click.option('--token', envvar='FASTLY_AUTH_TOKEN')
def get_all_versions(token, service):
    headers = {'Fastly-Key': token}
    return send_request("GET", URL_FORMAT % ("/service/%s/version" % service), headers,
                        None)
