#!/usr/bin/env python2.7

import numpy as np
import scipy
import sys
import scipy.spatial.distance as sp

POINTS = 6667

if __name__ == "__main__":
	points = []
	for line in sys.stdin:
		line = line.strip()
		features = np.fromstring(line, sep=' ')
		points.append(features)

	rate = 0.001
	num_samples = 200 #rate*len(points)
	rand_points = np.random.random_integers(0,POINTS,num_samples)
	coresets = []

	key = 1
	for i in rand_points:
		coresets.append(points[i].tolist())
		#print "%s\t%s" % (key, points[i].tolist())

	k = 10
	min_weight = 1
	max_weight = 0 
	hash_map = {}

	weights = []

	distances = sp.cdist(coresets, coresets,'euclidean')
	for i in range(0, len(coresets)):
		# find the K nearest neigbours
		# print distances[i]
		nearest_neighbors_idx = sorted(range(len(distances[i])),key=lambda x:distances[i][x])
	        nearest_neighbors_idx = nearest_neighbors_idx[0:k]
		weight = 0
	        for j in nearest_neighbors_idx:
			d = sp.cdist([coresets[i]], [coresets[j]])
	        	weight = weight + d[0][0]
		if min_weight > weight:
			min_weight = weight
		if max_weight < weight:
			max_weight < weight
		weights.append(1.0/(weight/(k+0.0)))

	for i in range(0, len(coresets)):
		weight = ((weights[i] + min_weight) / (min_weight + max_weight + 0.0))
		if np.random.rand() < weight:
        		print "%s\t%s" % (weight, coresets[i])		 





