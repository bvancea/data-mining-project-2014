#!/usr/bin/env python2.7

# This function has to either stay in this form or implement the
# feature mapping. For details refer to the handout pdf.
import sys
import numpy as np

FEATURE_SIZE = 400
SEPARATOR = ' '
LAMBDA = 100
LEARNING_RATE = 0.5
#LAMBDA = 4.0
#LEARNING_RATE = 1


def linear(x, y):
    return np.inner(x, y)


def polynomial(x, y, d):
    return (np.inner(x, y))**d


def kernel(x, y):
    #return linear(x, y)
    return polynomial(x, y, 3)


def transform(x_original):
    #x_2 = np.power(x_original, 2)
    #x_2 = np.sin(x_original)
    #x_original = np.append(x_original, x_2)
    return x_original


def process_line(line):
    line = line.strip()
    label, features = line.split(SEPARATOR, 1)
    y = int(label)
    x = np.fromstring(features, sep=SEPARATOR)
    x = transform(x)
    return x, y


def perform_descent_step(w, x, y):
    if y * kernel(x, w) < 1:
        w_prime = w + LEARNING_RATE * y * x
        prod = kernel(w_prime, w_prime)
        #print(prod)
        #prod = np.array(prod)[0][0]
        #prod = 1
        w_projection = 1.0 / np.sqrt(LAMBDA * prod)
        w = w_prime * min(1.0, w_projection)
    return w


def main():
    w = np.zeros(FEATURE_SIZE * 1)

    for line in sys.stdin:
        x, y = process_line(line)
        w = perform_descent_step(w, x, y)

    key = 0
    value = np.array(w).flatten()
    value = list(value)
    print "%s\t%s" % (key, value)


if __name__ == "__main__":
    main()