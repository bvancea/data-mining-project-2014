#!/usr/bin/env python2.7

# This function has to either stay in this form or implement the
# feature mapping. For details refer to the handout pdf.
import sys
import numpy as np

FEATURE_SIZE = 400
SEPARATOR = ' '
LAMBDA = 0.001
LEARNING_RATE = 0.001


def transform(x_original):
    return x_original


def process_line(line):
    line = line.strip()
    label, features = line.split(SEPARATOR, 1)
    y = int(label)
    x = np.fromstring(features, sep=SEPARATOR)
    x = np.mat(x)
    return x, y


def perform_descent_step(w, x, y):
    if y * w * x.transpose() < 1:
        w_prime = w + LEARNING_RATE * y * x
        w_projection = 1 / np.sqrt(LAMBDA, w_prime * w_prime.transpose())
        w = w_prime * min(1, w_projection)
    return w


def main():
    w = np.zeros(FEATURE_SIZE)
    w = np.mat(w)

    #TODO randomly pick points
    for line in sys.stdin:
        x, y = process_line(line)
        w = perform_descent_step(w, x, y)

    key = 0
    value = np.array(w).flatten()
    value = list(value)
    print "%s\t%s" % (key, value)


if __name__ == "__main__":
    main()