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


def partition(video_id, shingles):
    #hash document
    hashed_shingles = [hash_f(hash_func, x) for x in shingles]
    print "%s\t%s" % (min(hashed_shingles), video_id)


if __name__ == "__main__":
    # Very important. Make sure that each machine is using the
    # same seed when generating random numbers for the hash functions.
    np.random.seed(seed=42)
    hash_func = generate_hash_function()

    for line in sys.stdin:
        line = line.strip()
        video_id = int(line[6:15])
        shingles = np.fromstring(line[16:], sep=" ")
        partition(video_id, shingles)



