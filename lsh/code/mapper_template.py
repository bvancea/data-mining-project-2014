#!/usr/bin/env python

import numpy as np
import sys

r = 8
b = 16
n = 100000


def generate_hash_function():
    return np.random.random_integers(1, 10000, 3)


def generate_hash_functions(size):
    return [generate_hash_function() for _ in range(0, size)]


def compute_hash(hash_func, shingle):
    a = hash_func[0]
    b = hash_func[1]
    c = hash_func[2]
    return (a * shingle + b) % c


def generate_band_hash(size):
    band_hash = np.random.random_integers(1, 10000, size + 1)
    return band_hash


def generate_band_hash_functions(size):
    return [generate_band_hash(size) for _ in range(0, b)]


def compute_band_hash(band, hash_function):
    sum = hash_function[len(band)]
    for i in range(0, len(band)):
        sum += band[i] * hash_function[i]
    return sum % n


def compute_min_hash(hash_func, shingles):
    hashed_shingles = [compute_hash(hash_func, x) for x in shingles]
    return min(hashed_shingles)


def compute_hash_for_functions(hash_functions, shingles):
    sign_matrix_col = [compute_min_hash(hash_func=hf, shingles=shingles) for hf in hash_functions]
    return sign_matrix_col


def hash_signature_column(signature_column):
    band_hashes = list()
    for i in range(0, b):
        start_index = i * r
        end_index = start_index + r
        band = signature_column[start_index:end_index]
        band_hashes.append(compute_band_hash(band, band_hash_functions[i]))
    return band_hashes


def partition(video_id, shingles):
    #hash document
    hashed_shingles = compute_hash_for_functions(hash_functions=hash_functions, shingles=shingles)
    signature_column = np.array(hashed_shingles)
    band_hashes = hash_signature_column(signature_column)
    for key in band_hashes:
        print "%s\t%s" % (key, (video_id, shingles.tolist()))


if __name__ == "__main__":
    # Very important. Make sure that each machine is using the
    # same seed when generating random numbers for the hash functions.
    np.random.seed(seed=42)
    hash_functions = generate_hash_functions(r * b)
    band_hash_functions = generate_band_hash_functions(r)
    for line in sys.stdin:
        line = line.strip()
        video_id = int(line[6:15])
        shingles = np.fromstring(line[16:], sep=" ")
        partition(video_id, shingles)



