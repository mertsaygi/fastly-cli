import click
import vcl
import version
import os


@click.group()
def entry_point():
    if "FASTLY_AUTH_TOKEN" not in os.environ:
        raise Exception("FASTLY_AUTH_TOKEN is not exist in environment variables. Please define your token to your environment!")

entry_point.add_command(vcl.upload_vcl)
entry_point.add_command(vcl.get_all_vcls)

entry_point.add_command(version.clone_version)
entry_point.add_command(version.activate_version)
entry_point.add_command(version.get_version)
entry_point.add_command(version.get_all_versions)
