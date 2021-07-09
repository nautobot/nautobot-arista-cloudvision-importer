"""Diffsync models for Nautobot <-> CloudVision sync."""

from diffsync import DiffSyncModel
from typing import List

import nautobot_aristacv_importer.diffsync.cvutils as cvutils
import nautobot_aristacv_importer.diffsync.nbutils as nbutils
import time

class UserTag(DiffSyncModel):
    """Tag model"""

    _modelname = "tag"
    _identifiers = ("name", "value")
    _attributes = ("devices",)

    name: str
    value: str
    devices: List = list()

    @classmethod
    def create(cls, diffsync, ids, attrs):
        """Create a tag in Nautobot."""
        tag_name = f"{ids['name']}:{ids['value']}"
        tag_slug = f"arista_{ids['name'].lower()}_{ids['value'].lower()}"
        nbutils.create_tag(tag_name, tag_slug)
        for device in attrs["devices"]:
            nb_device = nbutils.get_device(device)
            nbutils.assign_tag(nb_device, tag_slug)
        return super().create(ids=ids, diffsync=diffsync, attrs=attrs)

    def update(self, attrs):
        #remove = set(self.devices) - set(attrs["devices"])
        #add = set(attrs["devices"]) - set(self.devices)
        ## Create mapping from device_name to CloudVision device_id
        #device_ids = {dev["hostname"]: dev["device_id"] for dev in cvutils.get_devices()}
        #for device in remove:
        #    cvutils.remove_tag_from_device(device_ids[device], self.name, self.value)
        #for device in add:
        #    # Exclude devices that are inactive in CloudVision
        #    if device in device_ids:
        #        cvutils.assign_tag_to_device(device_ids[device], self.name, self.value)
        #    else:
        #        tag = f"{self.name}:{self.value}" if self.value else self.name
        #        self.diffsync.job.log_warning(
        #            message=f"{device} is inactive or missing in CloudVision - skipping for tag: {tag}"
        #        )
        # Call the super().update() method to update the in-memory DiffSyncModel instance
        return super().update(attrs)

    def delete(self):
        """Delete user tag applied to devices in CloudVision."""
        #device_ids = {dev["hostname"]: dev["device_id"] for dev in cvutils.get_devices()}
        #for device in self.devices:
        #    cvutils.remove_tag_from_device(device_ids[device], self.name, self.value)
        #cvutils.delete_tag(self.name, self.value)
        ## Call the super().delete() method to remove the DiffSyncModel instance from its parent DiffSync adapter
        #super().delete()
        return self
