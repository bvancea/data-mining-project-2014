#!/usr/bin/env python2.7
import sys
import numpy as np

SEPARATOR = ' '
POINTS = 6667


def main():
    aggr_features = None
    count = 0
    indexes = np.random.random_integers(0, POINTS, 400)
    indexes = sorted(indexes)
    for line in sys.stdin:
        if count in indexes:
            line = line.strip()
            features = np.fromstring(line, sep=SEPARATOR)
            if aggr_features is None:
                aggr_features = features
            else:
                aggr_features = np.vstack((aggr_features, features))
        count += 1

    for point in aggr_features:
        key = 1
        value = point.tolist()
        print "%s\t%s" % (key, value)

if __name__ == "__main__":
    main()
