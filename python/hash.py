#!/usr/bin/python3
import hashlib
import argparse

# Instantiate the parser
parser = argparse.ArgumentParser(description='Illustrating bitcoin mining')

# Require 1 positional argument & Parse and access arguments
parser.add_argument('number_of_zeroes', type=int, help='REQUIRED: the amount of leading zeroes')
args = parser.parse_args()
number_of_zeroes = args.number_of_zeroes

# Init the hash object
h = hashlib.new('sha256')
h.update(b"Nobody inspects")
digest = h.hexdigest()
nonce=0

# As long as there is no sufficient amount of leading zeros
while(digest[0:number_of_zeroes] != "0"*number_of_zeroes):
    # Increment the nonce
    nonce += 1 

    # Calculate a new hash
    h = hashlib.new('sha256')
    h.update(b"Nobody inspects")
    h.update(str(nonce).encode(encoding='UTF-8'))

    # Get & print the digest
    digest = h.hexdigest()
    print( digest )

# Show summary
print("I needed %d attempts" % (nonce))