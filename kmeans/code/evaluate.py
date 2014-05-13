from scipy.spatial.distance import euclidean
import sys

__author__ = 'bogdan'

import numpy as np


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

if len(sys.argv) < 3:
    print "Usage: python evaluate.py training_file centers_file"
    exit(-1)

training_file_name = sys.argv[1]
centers_file_name = sys.argv[2]

data = np.loadtxt(training_file_name)
centers = np.loadtxt(centers_file_name)
n_points = 100000

print "Cost: %d" % compute_cost(data, n_points, centers)