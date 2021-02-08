#! /usr/bin/env python
from getpass import getpass
from netmiko import ConnectHandler, file_transfer

password = getpass()

nxos1 = {
    "device_type": "cisco_nxos”,
    "host": “nexus1.lasthop.io",
    "username": "pyclass",
    "password": password,
}

source_file = “testx.txt”
dest_file = “testx.txt”
direction = “put”.  <— You can toggle this to be a “get”
file_system = “bootflash:”

# Create the Netmiko SSH connection
ssh_conn = ConnectHandler(**nxos1)
transfer_dict = file_transfer(
    ssh_conn,
    source_file=source_file,
    dest_file=dest_file,
    file_system=file_system,
    direction=direction,
    overwrite_file=true,
)
print(transfer_dict)

