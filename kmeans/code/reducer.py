#!/usr/bin/env python2.7
import numpy as np
from scipy.spatial.distance import cdist, euclidean
import sys

CLUSTERS = 200


def online_kmeans(data, n_clusters, n_points):
    #randomly assign clusters
    center_indices = np.random.random_integers(0, n_points - 1, n_clusters)
    centers = np.copy(data[center_indices])
    cluster_counts = np.zeros(n_clusters)

    #apply online update for all points
    for point in data:
        min_value = sys.maxint
        min_index = 0
        index = 0

        #find nearest center
        for center in centers:
            dist = euclidean(center, point)
            if dist < min_value:
                min_index = index
                min_value = dist
            index += 1

    #update count
    cluster_counts[min_index] += 1
    centers[min_index] += (1 / cluster_counts[min_index]) * (point - centers[min_index])
    return centers


def compute_cost(data, n_points, centers):
    cost = 0
    for point in data:
        min_value = sys.maxint
        index = 0

        #find nearest center
        for center in centers:
            dist = euclidean(center, point)
            if dist < min_value:
                min_value = dist
            index += 1
        cost += (min_value * min_value)

    cost = cost / n_points
    return cost


def main():
    #kmeans = cluster.KMeans(n_clusters=CLUSTERS, max_iter=ITERATIONS)
    points = None
    count = 0
    for line in sys.stdin:
        count += 1
        line = line.strip()
        key, value = line.split("\t")
        point = np.array(eval(value))
        if points is None:
            points = point
        else:
            points = np.vstack((points, point))

    #kmeans.fit(points)
    centers = online_kmeans(points, CLUSTERS, count)
    #print "Cost: %d" % compute_cost(points, count, centers)

    for center in centers:
        print(' '.join(map(str, center)))

if __name__ == "__main__":
    main()
