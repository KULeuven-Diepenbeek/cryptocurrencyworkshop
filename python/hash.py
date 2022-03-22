#!/usr/bin/python3

import hashlib


import argparse

# Instantiate the parser
parser = argparse.ArgumentParser(description='Illustrating bitcoin mining')

# Require 1 positional argument
parser.add_argument('number_of_zeroes', type=int, help='REQUIRED: the amount of leading zeroes')

# Parse arguments
args = parser.parse_args()

# Access the arguments
number_of_zeroes = args.number_of_zeroes



h = hashlib.new('sha256')
h.update(b"Nobody inspects")
digest = h.hexdigest()
print( digest )
i=0

while(digest[0:number_of_zeroes] != "0"*number_of_zeroes) :
    i += 1 
    h = hashlib.new('sha256')
    h.update(b"Nobody inspects")
    h.update(str(i).encode(encoding='UTF-8'))
    digest = h.hexdigest()
    print( digest )

print("I needed %d attempts" % (i+1))