#!/usr/bin/env python2.7
import numpy as np
from scipy.spatial.distance import euclidean
import sys

CLUSTERS = 200


def online_kmeans(data, weights, n_clusters, n_points):
    #randomly assign clusters
    center_indices = np.random.random_integers(0, n_points - 1, n_clusters)
    centers = np.copy(data[center_indices])
    cluster_counts = np.zeros(n_clusters)

    index_point = 0
    #apply online update for all points
    for point in data:
        min_value = sys.maxint
        min_index = 0
        index = 0
        #find nearest center
        for center in centers:
            dist = weights[index_point] * euclidean(center, point)
            if dist < min_value:
                min_index = index
                min_value = dist
            index += 1

        #update count
        cluster_counts[min_index] += 1
        centers[min_index] += (weights[index_point] / cluster_counts[min_index]) * (point - centers[min_index])
        index_point += 1

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
    points = None
    count = 0
    weights = np.array([])
    for line in sys.stdin:
        count += 1
        line = line.strip()
        key, value = line.split("\t")
        point = np.array(eval(value))
        weights = np.append(weights, float(key))
        if points is None:
            points = point
        else:
            points = np.vstack((points, point))

    #kmeans.fit(points)
    centers = online_kmeans(points, weights, CLUSTERS, count)

    for center in centers:
        print(' '.join(map(str, center)))

    #print "Cost: %d" % compute_cost(points, count, centers)


if __name__ == "__main__":
    main()
