#!/usr/bin/env python2.7
import sys
import numpy as np

SEPARATOR = ' '


def main():
    for line in sys.stdin:
        line = line.strip()
        features = np.fromstring(line, sep=SEPARATOR)
        value = features.tolist()
        print "%s\t%s" % (1, value)

if __name__ == "__main__":
    main()
