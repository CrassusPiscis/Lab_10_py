from Iter_1.Integrate import integrate
from Iter_4 import Integrate
import timeit
import math

def get_result_iter_1():
    time1_iter_1 = timeit.timeit(lambda: integrate(math.cos, 0, math.pi / 2, n_iter=100), number=100)
    time2_iter_1 = timeit.timeit(lambda: integrate(math.sin, 0, math.pi, n_iter=100), number=100)
    print(f"Время выполнения integrate math.cos, 0 to pi/2, 100 iter: {time1_iter_1}")
    print(f"Время выполнения integrate math.sin, 0 to pi, 100 iter: {time2_iter_1}")
    print("\n")

    return 0

def get_result_iter_4():
    time1_iter_4 = timeit.timeit(lambda: Integrate.integrate(math.cos, 0, math.pi / 2, n_iter=100),  number=100)
    time2_iter_4 = timeit.timeit(lambda: Integrate.integrate(math.sin, 0, math.pi, n_iter=100), number=100)
    print(f"Время выполнения integrate math.cos, 0 to pi/2, 100 iter: {time1_iter_4}")
    print(f"Время выполнения integrate math.sin, 0 to pi, 100 iter: {time2_iter_4}")
    print("\n")

    return 0
if __name__ == '__main__':
    print('Время выполнения Итерации 1:')
    get_result_iter_1()
    print('Время выполнения Итерации 4:')
    get_result_iter_4()
