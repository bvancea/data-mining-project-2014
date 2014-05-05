#!/usr/bin/env python2.7
import sys
import numpy as np
from sklearn.cluster import MiniBatchKMeans

SEPARATOR = ' '
CENTERS = 200


def main():
    kmeans = MiniBatchKMeans(n_clusters=CENTERS)
    aggr_features = None
    count = 0
    for line in sys.stdin:
        line = line.strip()
        features = np.fromstring(line, sep=SEPARATOR)
        if aggr_features is None:
            aggr_features = features
        else:
            aggr_features = np.vstack((aggr_features, features))

        if count == 500:
            kmeans.partial_fit(aggr_features)
            aggr_features = None
            count = 0
        else:
            count += 1

    if count != 0:
        kmeans.partial_fit(aggr_features)

    count = 0
    for center in kmeans.cluster_centers_:
        key = count
        value = list(center)
        print "%s\t%s" % (key, value)
        count += 1

if __name__ == "__main__":
    main()
