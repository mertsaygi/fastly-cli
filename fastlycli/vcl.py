import sys
from pkg_resources import iter_entry_points
from settings import *
import click
import urllib
import requests


@click.command()
@click.option('--service', required=True)
@click.option('--version', required=True)
@click.option('--name', required=True)
@click.option('--file', required=True)
@click.option('--token', envvar='FASTLY_AUTH_TOKEN')
def upload_vcl(token, service, version, name, file):
    data = open(file, 'r').read()
    # print data
    url = URL_FORMAT % ("/service/%s/version/%s/vcl" % (service, version))
    headers = {'Fastly-Key': token}
    payload = {'name': name, 'content': data}
    # print payload
    # payload = urllib.urlencode(payload, doseq=True)
    resp_data = requests.post(url, headers=headers, data=payload)
    print resp_data.text


@click.command()
@click.option('--service', required=True)
@click.option('--version', required=True, help='version number of vcl')
@click.option('--token', envvar='FASTLY_AUTH_TOKEN')
def get_all_vcls(token, service, version):
    url = URL_FORMAT % ("/service/%s/version/%s/vcl" % (service, version))
    headers = {'Fastly-Key': token}
    resp_data = requests.get(url, headers=headers)
    print resp_data.text
