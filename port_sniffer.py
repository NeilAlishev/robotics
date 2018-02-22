# Packet sniffer in python for Linux
# Sniffs only incoming TCP packet

import socket
import time
from struct import *


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    print("Packet sniffer is running...")

    # receive a packet
    while True:
        packet = s.recvfrom(65565)
        # packet string from tuple
        packet = packet[0]

        # take first 20 characters for the ip header
        ip_header = packet[0:20]

        # unpack ip header
        iph = unpack('!BBHHHBBH4s4s', ip_header)

        version_ihl = iph[0]
        ihl = version_ihl & 0xF
        iph_length = ihl * 4

        tcp_header = packet[iph_length:iph_length + 20]

        # unpack header
        tcph = unpack('!HHLLBBHHH', tcp_header)

        source_port = tcph[0]
        dest_port = tcph[1]

        # set port here.
        if dest_port == 8000:
            print("RECEIVED from port : {}".format(dest_port))

        # sleep for 1 second
        time.sleep(1)


main()
