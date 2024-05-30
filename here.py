import os
import sys
import numpy as np
import matplotlib.pyplot as plt


def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(x * w) + b
    if tmp > 0:
        return 1
    else:
        return 0


if __name__ == '__main__':
    print('hello world!')
    print(AND(1, 1))