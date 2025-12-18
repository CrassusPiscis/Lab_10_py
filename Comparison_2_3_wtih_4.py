from Iter_2.Integrate_async_thread import integrate_async_thread
from Iter_3.Integrate_async_process import integrate_async_process
from Iter_4 import Integrate
import timeit
import math

def get_result_iter_2():
    time1_iter_2 = timeit.timeit(lambda: integrate_async_thread(math.cos, 0, math.pi / 2, n_jobs=2, n_iter=100),  number=1)
    time2_iter_2 = timeit.timeit(lambda: integrate_async_thread(math.cos, 0, math.pi / 2, n_jobs=4, n_iter=100), number=1)
    time3_iter_2 = timeit.timeit(lambda: integrate_async_thread(math.cos, 0, math.pi / 2, n_jobs=6, n_iter=100), number=1)
    time4_iter_2 = timeit.timeit(lambda: integrate_async_thread(math.cos, 0, math.pi / 2, n_jobs=8, n_iter=100), number=1)

    time5_iter_2 = timeit.timeit(lambda: integrate_async_thread(math.sin, 0, math.pi, n_jobs=2, n_iter=100), number=1)
    time6_iter_2 = timeit.timeit(lambda: integrate_async_thread(math.sin, 0, math.pi, n_jobs=4, n_iter=100), number=1)
    time7_iter_2 = timeit.timeit(lambda: integrate_async_thread(math.sin, 0, math.pi, n_jobs=6, n_iter=100), number=1)
    time8_iter_2 = timeit.timeit(lambda: integrate_async_thread(math.sin, 0, math.pi, n_jobs=8, n_iter=100), number=1)

    print(f"Время выполнения integrate_async_thread math.cos, 0 to pi/2, 2 threads, 100 iter, 1 compilation: {time1_iter_2}")
    print(f"Время выполнения integrate_async_thread math.cos, 0 to pi/2, 4 threads, 100 iter, 1 compilation: {time2_iter_2}")
    print(f"Время выполнения integrate_async_thread math.cos, 0 to pi/2, 6 threads, 100 iter, 1 compilation: {time3_iter_2}")
    print(f"Время выполнения integrate_async_thread math.cos, 0 to pi/2, 8 threads, 100 iter, 1 compilation: {time4_iter_2}")
    print("\n")
    print(f"Время выполнения integrate_async_thread math.sin, 0 to pi, 2 threads,  100 iter, 1 compilation: {time5_iter_2}")
    print(f"Время выполнения integrate_async_thread math.sin, 0 to pi, 4 threads,  100 iter, 1 compilation: {time6_iter_2}")
    print(f"Время выполнения integrate_async_thread math.sin, 0 to pi, 6 threads,  100 iter, 1 compilation: {time7_iter_2}")
    print(f"Время выполнения integrate_async_thread math.sin, 0 to pi, 8 threads,  100 iter, 1 compilation: {time8_iter_2}")
    print("\n")

    return 0

def get_result_iter_3():


    time1_iter_3 = timeit.timeit(lambda: integrate_async_process(math.cos, 0, math.pi / 2, n_jobs=2, n_iter=100), number=1)
    time2_iter_3 = timeit.timeit(lambda: integrate_async_process(math.cos, 0, math.pi / 2, n_jobs=4, n_iter=100), number=1)
    time3_iter_3 = timeit.timeit(lambda: integrate_async_process(math.cos, 0, math.pi / 2, n_jobs=6, n_iter=100), number=1)
    time4_iter_3 = timeit.timeit(lambda: integrate_async_process(math.cos, 0, math.pi / 2, n_jobs=8, n_iter=100), number=1)

    time5_iter_3 = timeit.timeit(lambda: integrate_async_process(math.sin, 0, math.pi, n_jobs=2, n_iter=100), number=1)
    time6_iter_3 = timeit.timeit(lambda: integrate_async_process(math.sin, 0, math.pi, n_jobs=4, n_iter=100), number=1)
    time7_iter_3 = timeit.timeit(lambda: integrate_async_process(math.sin, 0, math.pi, n_jobs=6, n_iter=100), number=1)
    time8_iter_3 = timeit.timeit(lambda: integrate_async_process(math.sin, 0, math.pi, n_jobs=8, n_iter=100), number=1)

    print(f"Время выполнения integrate_async_process math.cos, 0 to pi/2, 2 processes, 100 iter, 1 compilation: {time1_iter_3}")
    print(f"Время выполнения integrate_async_process math.cos, 0 to pi/2, 4 processes, 100 iter, 1 compilation: {time2_iter_3}")
    print(f"Время выполнения integrate_async_process math.cos, 0 to pi/2, 6 processes, 100 iter, 1 compilation: {time3_iter_3}")
    print(f"Время выполнения integrate_async_process math.cos, 0 to pi/2, 8 processes, 100 iter, 1 compilation: {time4_iter_3}")
    print("\n")
    print(f"Время выполнения integrate_async_process math.sin, 0 to pi, 2 processes,  100 iter, 1 compilation: {time5_iter_3}")
    print(f"Время выполнения integrate_async_process math.sin, 0 to pi, 4 processes,  100 iter, 1 compilation: {time6_iter_3}")
    print(f"Время выполнения integrate_async_process math.sin, 0 to pi, 6 processes,  100 iter, 1 compilation: {time7_iter_3}")
    print(f"Время выполнения integrate_async_process math.sin, 0 to pi, 8 processes,  100 iter, 1 compilation: {time8_iter_3}")
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
    print('Время выполнения Итерации 2:')
    get_result_iter_2()
    print('Время выполнения Итерации 3:')
    get_result_iter_3()
    print('Время выполнения Итерации 4:')
    get_result_iter_4()
