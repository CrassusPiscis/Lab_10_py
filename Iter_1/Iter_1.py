from Integrate import integrate
import math
import timeit

def get_result():
    time1 = timeit.timeit(lambda: integrate(math.cos, 0, math.pi / 2, n_iter=100), number=100)
    time2 = timeit.timeit(lambda: integrate(math.sin, 0, math.pi, n_iter=100), number=100)
    print(f"Время выполнения integrate math.cos, 0 to pi/2, 100 iter: {time1}")
    print(f"Время выполнения integrate math.sin, 0 to pi, 100 iter: {time2}")

    return [time1, time2]

get_result()