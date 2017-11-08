#!/bin/bash

eval "sudo tcpdump -i any -s 0 -w result src net 192.168.2.0/24"

echo "Filtering out everything but internal traffic"

eval "sudo tcpdump -i any -s 0 -w result
src net 192.168.2.0/24 && dst net \
192.168.0.0/16"

echo "Filtering out everything but web traffic, identified by port"

eval "sudo tcpdump -i any -s 0 -w result
((src port 80 || src port 443) && \
(src net 192.168.2.0)"
