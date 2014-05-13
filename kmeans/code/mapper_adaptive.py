#!/usr/bin/env python2.7
from scipy import stats
import sys
import numpy as np
from scipy.spatial.distance import cdist

SEPARATOR = ' '
NR_SAMPLES = 100
NR_CORESETS = 1000


def simple_adaptive_sampling(data, n_points):
    #compute all pairwise distances
    distances = cdist(data, data)

    #declare weight vectors
    weights = {}
    q_weights = {}
    q_weight_normalizer = 1

    #uniformly sample some points
    sampled_indices = np.random.random_integers(0, n_points - 1, NR_CORESETS).tolist()
    for index in sampled_indices:
        min_dist = sys.maxint

        #compute a radius around this point corresponding more or less to a Voronoi cell
        for second_index in sampled_indices:
            if index != second_index:
                if distances[index][second_index] < min_dist:
                    min_dist = distances[index][second_index]

        #compute radius from diameter
        min_dist = min_dist

        #see how many points are inside the radius
        current_cell_weights = 0
        for distance in distances[index]:
            if distance < min_dist:
                current_cell_weights += distance

        #set weights
        q_weights[index] = current_cell_weights
        q_weight_normalizer += current_cell_weights

    for index in q_weights:
        q_weights[index] = q_weights[index] / q_weight_normalizer
        if q_weights[index] != 0:
            weights[index] = 1.0/(NR_CORESETS * q_weights[index])
        else:
            weights[index] = 0.0

    return weights, q_weights


def main():
    points = None
    count = 0
    for line in sys.stdin:
        line = line.strip()
        point = np.fromstring(line, sep=SEPARATOR)
        if points is None:
            points = point
        else:
            points = np.vstack((points, point))
        count += 1

    weights, q_weights = simple_adaptive_sampling(points, count)

    #construct a distribution form the q_weights
    qk = q_weights.keys()
    pk = q_weights.values()
    q_dist = stats.rv_discrete(name='q_dist', values=(qk, pk))
    for i in range(0, NR_SAMPLES):
        index = q_dist.rvs()
        print "%s\t%s" % (weights[index], points[index].tolist())

if __name__ == "__main__":
    main()