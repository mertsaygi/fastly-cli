from settings import *
import click
from helpers.helper import *


@click.command()
@click.option('--service', required=True)
@click.option('--version', required=True)
@click.option('--name', required=True)
@click.option('--file', required=True)
@click.option('--token', envvar='FASTLY_AUTH_TOKEN')
def upload_vcl(token, service, version, name, file):
    data = open(file, 'r').read()
    headers = {'Fastly-Key': token}
    payload = {'name': name, 'content': data}
    return send_request("POST", URL_FORMAT % ("/service/%s/version/%s/vcl" % (service, version)), headers, payload)


@click.command()
@click.option('--service', required=True)
@click.option('--version', required=True)
@click.option('--name', required=True)
@click.option('--token', envvar='FASTLY_AUTH_TOKEN')
def set_as_main_vcl(token, service, version, name):
    headers = {'Fastly-Key': token}
    return send_request("PUT", URL_FORMAT % ("/service/%s/version/%s/vcl/%s/main" % (service, version, name)), headers,
                        None)


@click.command()
@click.option('--service', required=True)
@click.option('--version', required=True)
@click.option('--name', required=True)
@click.option('--file', required=True)
@click.option('--token', envvar='FASTLY_AUTH_TOKEN')
def update_vcl(token, service, version, name, file):
    data = open(file, 'r').read()
    headers = {'Fastly-Key': token}
    payload = {'name': name, 'content': data}
    return send_request("PUT", URL_FORMAT % ("/service/%s/version/%s/vcl/%s" % (service, version, name)), headers,
                        payload)


@click.command()
@click.option('--service', required=True)
@click.option('--version', required=True, help='version number of vcl')
@click.option('--token', envvar='FASTLY_AUTH_TOKEN')
def get_all_vcls(token, service, version):
    headers = {'Fastly-Key': token}
    return send_request("GET", URL_FORMAT % ("/service/%s/version/%s/vcl" % (service, version)), headers,
                        None)


@click.command()
@click.option('--service', required=True)
@click.option('--version', required=True)
@click.option('--name', required=True)
@click.option('--token', envvar='FASTLY_AUTH_TOKEN')
def delete_vcl(token, service, version, name):
    headers = {'Fastly-Key': token}
    return send_request("DELETE", URL_FORMAT % ("/service/%s/version/%s/vcl/%s" % (service, version, name)), headers,
                        None)
