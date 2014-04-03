#!/usr/bin/env python2.7
import sys
import numpy as np


def main():
    count = 0
    w = None
    for line in sys.stdin:
        line = line.strip()
        key, value = line.split("\t")
        value = np.array(eval(value))
        if w is None:
            w = value
        else:
            w += value
        count += 1

    w = w / count
    params = [x for x in np.array(w).flatten()]
    print ' '.join(map(str, params))


if __name__ == "__main__":
    main()
