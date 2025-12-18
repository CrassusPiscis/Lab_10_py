# cython: language_level=3
# cython: boundscheck=False
# cython: wraparound=False
# cython: cdivision=True

import cython

@cython.boundscheck(False)
@cython.wraparound(False)
def integrate(f, double a, double b, int n_iter=1000):
    """
    Оптимизированная версия функции integrate
    """
    cdef double step = (b - a) / n_iter
    cdef double acc = 0.0
    cdef double x
    cdef int i

    for i in range(n_iter):
        x = a + i * step
        acc += f(x)

    return acc * step