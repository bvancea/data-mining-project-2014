#!/usr/bin/env python

import numpy as np
import sys


def generate_hash_function():
    return np.random.random_integers(1, 100, 3)


def generate_hash_functions(size):
    return [generate_hash_function() for _ in range(0, size)]


def compute_hash(hash_func, shingle):
    a = hash_func[0]
    b = hash_func[1]
    c = hash_func[2]
    return (a * shingle + b) % c


def compute_min_hash(hash_func, shingles):
    hashed_shingles = [compute_hash(hash_func, x) for x in shingles]
    return min(hashed_shingles)


def compute_hash_for_functions(hash_functions, shingles):
    sign_matrix_col = [compute_min_hash(hash_func=hf, shingles=shingles) for hf in hash_functions]
    return sign_matrix_col


def partition(video_id, shingles):
    #hash document
    hashed_shingles = compute_hash_for_functions(hash_functions=hash_functions, shingles=shingles)
    key = hashed_shingles
    print "%s\t%s" % (key, video_id)


if __name__ == "__main__":
    # Very important. Make sure that each machine is using the
    # same seed when generating random numbers for the hash functions.
    np.random.seed(seed=42)
    hash_functions = generate_hash_functions(128)
    for line in sys.stdin:
        line = line.strip()
        video_id = int(line[6:15])
        shingles = np.fromstring(line[16:], sep=" ")
        partition(video_id, shingles)



