#!/usr/bin/env python

import numpy as np
import sys


def similar(a, b):
    similarity = len(a.intersection(b))/(1.0 * len(a.union(b)))
    return similarity >= 0.85


def print_duplicates(videos, shingles_map):
    unique = np.unique(videos)
    for i in xrange(len(unique)):
        for j in xrange(i + 1, len(unique)):
            first_vid = min(unique[i], unique[j])
            second_vid = max(unique[i], unique[j])
            if similar(set(shingles_map[first_vid]), set(shingles_map[second_vid])):
                print "%d\t%d" % (first_vid, second_vid)


last_key = None
key_count = 0
duplicates = []
shingles_map = {}

for line in sys.stdin:
    line = line.strip()
    key, value = line.split("\t")
    value = eval(value)
    video_id = value[0]
    shingles = value[1]
    if last_key is None:
        last_key = key

    if key == last_key:
        duplicates.append(int(video_id))
    else:
        # Key changed (previous line was k=x, this line is k=y)
        print_duplicates(duplicates, shingles_map)
        duplicates = [int(video_id)]
        shingles_map = {}
        last_key = key

    shingles_map[video_id] = shingles
if len(duplicates) > 0:
    print_duplicates(duplicates, shingles_map)