import numpy as np
import numba
from numba import jit


@jit(nopython=True)
def go_fast(a):
    trace = 0.0
    for index in range(a.shape[0]):
        trace += np.tanh(a[index, index])
    return a + trace


x = np.arange(100).reshape(10, 10)
go_fast(x)
