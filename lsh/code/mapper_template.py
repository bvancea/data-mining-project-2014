#!/usr/bin/env python

import numpy as np
import sys


def generate_hash_function():
    return np.random.random_integers(1, 10000, 3)

def hash_f(hash_func, shingle):
    a = hash_func[0]
    b = hash_func[1]
    c = hash_func[2]
    return (a * shingle + b) % c

def generate_hash_function_signature(l):
    n = np.random.randint(1, 10000)
    a = np.random.randint(1, 10000, l)
    b = np.random.randint(1, 10000, l)
    return [n, a, b]

def hash_signature (signature_block, hash_f):
    n = hash_f[0]
    a = hash_f[1]
    b = hash_f[2]
    hash_sum = 0
    for i in range(0, len(signature_block)):
        hash_sum = a[i] * signature_block[i] + b[i]
    return hash_sum % n

def partition(video_id, shingles, hash_func):
    #hash document
    hashed_shingles = [hash_f(hash_func, x) for x in shingles]
    return min(hashed_shingles)
    #print "%s\t%s" % (min(hashed_shingles), video_id)

if __name__ == "__main__":
    # Very important. Make sure that each machine is using the
    # same seed when generating random numbers for the hash functions.
    np.random.seed(seed=42)

    no_hash_f = 20
    hash_f_array = []

    for i in range(0, no_hash_f):
        hash_f_array.append(generate_hash_function())

    signature_matrix = []

    no_blocks = 5

    for line in sys.stdin:
        line = line.strip()
        video_id = int(line[6:15])
        shingles = np.fromstring(line[16:], sep=" ")
        s = shingles
        v = video_id

        # apply min-hash algorithm
	signature = no_hash_f*[0]
	for h in range(0, no_hash_f):
		signature[h] = partition(video_id, shingles, hash_f_array[h])

	# split the signature in block
        block_signatures = []
        for i in xrange(0, len(signature) - no_blocks, no_blocks):
            block = signature[i:i+no_blocks]
            # generate hash function
            signature_hash_f = generate_hash_function_signature(len(block))
            block_signatures.append(hash_signature(block, signature_hash_f))

        # treat last block separately
        if (i+no_blocks != len(signature)-1):
            block = signature[i+no_blocks:len(signature)]
            # generate hash function
            signature_hash_f = generate_hash_function_signature(len(block))
            block_signatures.append(hash_signature(block, signature_hash_f))
	print "%s\t%s" % (block_signatures, video_id)



