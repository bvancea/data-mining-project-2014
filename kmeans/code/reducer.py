#!/usr/bin/env python2.7
import sys
import numpy as np

MAPPERS = 300


def main():
    centers = {}
    for line in sys.stdin:
        line = line.strip()
        key, value = line.split("\t")
        center_point = np.array(eval(value))

        if key in centers:
            centers[key] = centers[key] + center_point/300
        else:
            centers[key] = center_point/300

    for key in centers:
        center_value = [x for x in centers[key]]
        print(' '.join(map(str, center_value)))

if __name__ == "__main__":
    main()
