import sys
from pkg_resources import iter_entry_points
from settings import *
import click
import urllib
import requests


@click.command()
@click.option('--service', required=True)
@click.option('--version', required=True, help='version number of vcl')
@click.option('--token', envvar='FASTLY_AUTH_TOKEN')
def clone_version(token, service, version):
    url = URL_FORMAT % ("/service/%s/version/%s/clone" % (service, version))
    headers = {'Fastly-Key': token}
    resp_data = requests.put(url, headers=headers)
    print resp_data.text


@click.command()
@click.option('--service', required=True, help='Fastly service name')
@click.option('--version', required=True, help='version number of vcl')
@click.option('--token', envvar='FASTLY_AUTH_TOKEN')
def activate_version(token, service, version):
    url = URL_FORMAT % ("/service/%s/version/%s/activate" % (service, version))
    headers = {'Fastly-Key': token}
    resp_data = requests.put(url, headers=headers)
    print resp_data.text


@click.command()
@click.option('--service', required=True)
@click.option('--version', required=True, help='version number of vcl')
@click.option('--token', envvar='FASTLY_AUTH_TOKEN')
def get_version(token, service, version):
    url = URL_FORMAT % ("/service/%s/version/%s" % (service, version))
    headers = {'Fastly-Key': token}
    resp_data = requests.get(url, headers=headers)
    print resp_data.text


@click.command()
@click.option('--service', required=True)
@click.option('--token', envvar='FASTLY_AUTH_TOKEN')
def get_all_versions(token, service):
    url = URL_FORMAT % ("/service/%s/version" % service)
    headers = {'Fastly-Key': token}
    resp_data = requests.get(url, headers=headers)
    print resp_data.text
