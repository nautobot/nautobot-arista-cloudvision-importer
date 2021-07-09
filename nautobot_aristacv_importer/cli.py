"""Example cli using click."""
import click
from .config import SETTINGS, Settings, load
from .diffsync.cvutils import connect_cv, get_tags_by_type, get_devices, disconnect_cv
from .diffsync.nbutils import connect_nb
from .diffsync.cloudvision import CloudVision
from .diffsync.nautobot import Nautobot
import pdb
# Import necessary project related things to use in CLI


@click.command()
# @click.option("--nautobot_server", default="127.0.0.1:8000", help="IP or hostname of Nautobot instance.")
# @click.option("--cloudvision_server", default="www.arista.io:443", help="IP or hostname of Cloudvision instance.")
# @click.option("--cvaas_token_file")
def main():
    """Sync user tags from Cloudvision to Nautobot."""
    settings = load().dict()

    # Load Cloudvision user tags
    print("Connecting to Cloudvision.")
    connect_cv(settings)
    cv = CloudVision()
    cv.load()

    # Load Nautobot tags
    print("Connecting to Nautobot.")
    connect_nb(settings["nautobot_url"], settings["nautobot_token"])
    nb = Nautobot()
    nb.load()

    print("Performing diff between Nautobot and Cloudvision.")
    diff = nb.diff_from(cv)
    print(diff.summary())
    nb.sync_from(cv)

    print("Disconnecting from Cloudvision.")
    disconnect_cv()
