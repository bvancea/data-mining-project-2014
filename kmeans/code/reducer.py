#!/usr/bin/env python2.7
import sys
import numpy as np
from sklearn import cluster

CLUSTERS = 200
ITERATIONS = 40


def main():
    kmeans = cluster.KMeans(n_clusters=CLUSTERS, max_iter=ITERATIONS)
    points = None
    for line in sys.stdin:
        line = line.strip()
        key, value = line.split("\t")
        point = np.array(eval(value))
        if points is None:
            points = point
        else:
            points = np.vstack((points, point))

    kmeans.fit(points)

    for center in kmeans.cluster_centers_:
        print(' '.join(map(str, center)))

if __name__ == "__main__":
    main()
