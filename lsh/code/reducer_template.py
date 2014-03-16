#!/usr/bin/env python

import numpy as np
import sys
import ast

def print_duplicates(videos):
    unique = np.unique(videos)
    for i in xrange(len(unique)):
        for j in xrange(i + 1, len(unique)):
            print "%d\t%d" % (min(unique[i], unique[j]),
                              max(unique[i], unique[j]))

last_key = None
key_count = 0
duplicates = []
hash_functions = []

for line in sys.stdin:
    line = line.strip()
    key, video_id = line.split("\t")

    key = ast.literal_eval(key)
    hash_functions.append(key)

    # AND hash functions

    if last_key is None:
        last_key = key

    if key == last_key:
        duplicates.append(int(video_id))
    else:
        # Key changed (previous line was k=x, this line is k=y)
        print_duplicates(duplicates)
        duplicates = [int(video_id)]
        last_key = key


'''
print hash_functions
print len(hash_functions)
print len(hash_functions[0])

#hash_functions = np.asarray(hash_functions).T.tolist()
hash_functions = map(list, zip(*hash_functions))

print hash_functions[0]

# OR hash funcitons
for i in range(0,len(hash_functions)):
    # tale the i-th column
    column = hash_functions[i]

    print "---" 
    print column

    column = column.sort()

    print len(column)

    last_key = None

    for j in range(0, len(column)):
        key = column[j]       

        if last_key is None:
            last_key = key

        if key == last_key:
            duplicates.append(int(video_id))
        else:
            # Key changed (previous line was k=x, this line is k=y)
            print_duplicates(duplicates)
            duplicates = [int(video_id)]
            last_key = key

if len(duplicates) > 0:
    print_duplicates(duplicates)
'''
