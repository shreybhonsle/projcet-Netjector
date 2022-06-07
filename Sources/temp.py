# import signal
# import sys

# def signal_handler(sig, frame):
#     print('\b\bYou pressed Ctrl+C!')
#     sys.exit(0)

# signal.signal(signal.SIGINT, signal_handler)
# print('Press Ctrl+C')
# import time
# time.sleep(30)
# import subprocess
# import re
# interface = input("Enter the interface : ")
# c = subprocess.check_output(["ifconfig",interface],stderr=subprocess.DEVNULL)
# c= c.decode('utf-8')
# pat = re.compile('\d+.\d+.\d+.\d+')
# op = pat.findall(c)
# ip = op[0]
# subnet = op[1]
# subnet = subnet.split('.')
# mask= 0
# for i in subnet:
#     if i == '255':
#         mask +=8
# print(mask)
# ip = ip+str('/')+str(mask)
# print(ip)
# c = subprocess.check_output(["netdiscover","-r",ip],stderr=subprocess.DEVNULL)
# c= c.decode('utf-8')
# print(c)
#c = subprocess.check_output(["netdi"])


import scapy.all as scapy

def scanNetwork(ip):
    arpPacket = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arpRequest = broadcast/arpPacket
    answered,unanswered = scapy.srp(arpRequest)
    print(answered,unanswered)
    
scanNetwork('172.17.4.0/16')