#!/usr/bin/env python

import numpy as np
import sys


class MultiDictN:
    def __init__(self):
        self.data = {}

    def put(self, key, value):
        if key in self.data:
            self.data[key].append(value)
        else:
            self.data[key] = [int(value)]

    def get(self, key):
        return self.data[key]

    def contains(self, key):
        return key in self.data

    def internal_data(self):
        return self.data.iteritems()

    def clear(self):
        self.data = {}


def generate_hash_function():
    return np.random.random_integers(1, 10000, 3)


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


def find_duplicates(hash_functions, signature_matrix, video_ids, r, b):
    document_map = MultiDictN()
    rounds = []
    c = 0
    for i in range(0, b):
        start_index = i * r
        end_index = start_index + r
        #print "Checking range : %s\t%s" % ( start_index, end_index )
        slice = signature_matrix[:, start_index:end_index]
        #print slice
        hash_function = hash_functions[i]
        k = 0
        for document in slice:
            min_hash = compute_min_hash(hash_function, document)
            document_map.put(key=min_hash, value=k)
            k += 1
        buckets = [None] * len(video_ids)
        for key, value in document_map.internal_data():
            for video_index in value:
                buckets[video_index] = key
        rounds.append(buckets)
        c += 1
        document_map.clear()

    for i in range(0, len(video_ids)):
        for j in range(0, len(video_ids)):
            candidate_pair = False
            times_equal = 0
            for k in range(0, c):
                if rounds[k][i] == rounds[k][j]:
                    times_equal += 1
            if times_equal / (c * 1.0) >= 0.83:
                candidate_pair = True
            if candidate_pair:
                #if np.array_equal(signature_matrix[i], signature_matrix[j]):
                print_duplicates_single(video_ids[i], video_ids[j])


def print_duplicates_single(video_id_1, video_id_2):
    print "%d\t%d" % (min(video_id_1, video_id_2),
                      max(video_id_2, video_id_1))


def print_duplicates(videos):
    unique = np.unique(videos)
    for i in xrange(len(unique)):
        for j in xrange(i + 1, len(unique)):
            print "%d\t%d" % (min(unique[i], unique[j]),
                              max(unique[i], unique[j]))

last_key = None
key_count = 0
duplicates = []
signature = []
video_ids = []
r = 2
b = 50

np.random.seed(seed=12)
hash_functions = generate_hash_functions(b)

for line in sys.stdin:
    line = line.strip()
    key, value = line.split("\t")
    value = eval(value)
    column = value[0]
    video_id = value[1]
    if last_key is None:
        last_key = key
    if key == last_key:
        signature.append(column)
        video_ids.append(video_id)
    else:
        signature_matrix = np.array(signature)
        find_duplicates(hash_functions=hash_functions,
                        signature_matrix=signature_matrix,
                        video_ids=video_ids,
                        r=r,
                        b=b)
        signature = [column]
        video_ids = [video_id]
        last_key = key


signature_matrix = np.array(signature)
#print signature_matrix
find_duplicates(hash_functions=hash_functions,
                signature_matrix=signature_matrix,
                video_ids=video_ids,
                r=r,
                b=b)


    #hash_map.put(key=key, value=value)

#for key, value in hash_map.internal_data():
#    print key, value
        #signature_matrix, video_ids = unzip_array_tuples(value)
        #print signature_matrix, video_ids
    #if last_key is None:
    #    last_key = key
    #
    #if key == last_key:
    #    duplicates.append(int(video_id))
    #else:
    #    # Key changed (previous line was k=x, this line is k=y)
    #    print_duplicates(duplicates)
    #    duplicates = [int(video_id)]
    #    last_key = key

#
#if len(duplicates) > 0:
#    print_duplicates(duplicates)
