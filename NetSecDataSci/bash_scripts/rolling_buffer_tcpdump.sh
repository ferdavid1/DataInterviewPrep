#!/bin/bash

eval "sudo tcpdump -i any -s 0 -w result -C 128 -W 32";

# The process writes approximately 128 MB to the 
# disk, (specified by the -C ), and then rotates
# to a new file. After 32 files are filled 
# (specified by the -W), the process restarts
