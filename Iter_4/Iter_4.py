import math
import timeit
import Integrate_optimized

def get_result():
    time1 = timeit.timeit(lambda: Integrate_optimized.integrate(math.cos, 0, math.pi / 2, n_iter=100),  number=100)
    time2 = timeit.timeit(lambda: Integrate_optimized.integrate(math.sin, 0, math.pi, n_iter=100), number=100)
    print(f"Время выполнения integrate math.cos, 0 to pi/2, 100 iter: {time1}")
    print(f"Время выполнения integrate math.sin, 0 to pi, 100 iter: {time2}")
    return time1, time2

if __name__ == "__main__":
    get_result()


# GIL
# Время выполнения integrate math.cos, 0 to pi/2, 100 iter: 0.0008084001019597054
# Время выполнения integrate math.sin, 0 to pi, 100 iter: 0.0007646000012755394

# noGIL
# Время выполнения integrate math.cos, 0 to pi/2, 100 iter: 0.0006927000358700752
# Время выполнения integrate math.sin, 0 to pi, 100 iter: 0.0006904997862875462