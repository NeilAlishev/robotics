#!/usr/bin/env python
# Packet sniffer in python for Linux

import socket
from struct import *

import rospy
import roslaunch
from std_msgs.msg import String

def main():
    pub = rospy.Publisher('packets', String, queue_size=10)
    rospy.init_node('packet_sniffer')
    rospy.loginfo('Packet sniffer node started')

    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))

    connection_on = True
    first_run = True
    error_counter = 0 # when it's 10, it's an error
    # receive a packet
    while True:
    	if (not connection_on) and (not first_run):
    		rospy.loginfo("Going back to the base")

        packet = s.recvfrom(65565)

        # packet string from tuple
        packet = packet[0]

        # parse ethernet header
        eth_length = 14
        eth_header = packet[:eth_length]
        eth = unpack('!6s6sH', eth_header)
        eth_protocol = socket.ntohs(eth[2])

        protocol = None
        # Parse IP packets, IP Protocol number = 8
        if eth_protocol == 8:
            # Parse IP header
            # take first 20 characters for the ip header
            ip_header = packet[eth_length:20 + eth_length]
            # now unpack them :)
            iph = unpack('!BBHHHBBH4s4s', ip_header)
            version_ihl = iph[0]
            version = version_ihl >> 4
            ihl = version_ihl & 0xF
            iph_length = ihl * 4
            ttl = iph[5]
            protocol = iph[6]
            s_addr = socket.inet_ntoa(iph[8])
            d_addr = socket.inet_ntoa(iph[9])

        # UDP packets
        if protocol == 17:
            u = iph_length + eth_length
            udph_length = 8
            udp_header = packet[u:u + 8]
            # now unpack them :)
            udph = unpack('!HHHH', udp_header)
            source_port = udph[0]
            dest_port = udph[1]
            length = udph[2]
            checksum = udph[3]
            if dest_port == 10000:
                rospy.loginfo("RECEIVED!")
                connection_on = True
                error_counter = 0
                first_run = False
            else:
            	if error_counter < 10:
            		error_counter += 1
            	else:
            		connection_on = False

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass