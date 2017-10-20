#MUST RUN WITH SUDO
from scapy.all import *
conf.verb = 0

p = IP(dst="github.com")/TCP()
r = sr1(p)
print(r.summary())

