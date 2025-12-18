import math
import timeit
from Iter_2.Integrate_async_thread import integrate_async_thread
from Iter_5 import Integrate_optimized
'''
    Обобщенный вывод сравнение времени работы многопоточной версии
    функции Integrate с Cythonized-версией Integrate:

    На малых количествах потоков (2, 4 потока) в многопоточной версии в сравнении
    noGIL и GIL разница во времени - незначительна - время выполнения GIL и noGIL примерно одинаковая 

    На больших количествах потоков (6, 8 потоков) в многопоточной версии в сравнении
    noGIL и GIL разница во времени - большая - noGIL справляется быстрее

    Однако, было замечено, что при использовании noGIL для Cython-версии Integrate
    время её выполнения становилось куда большим, чем с GIL

    Скорее всего, это связано с наличием Python-вызовов в Cythonized-коде, что 
    создает применение GIL, поэтому необходимо как можно больше увеличить
    процент чистого C-кода в Cython-файле, либо полностью написать его на C
'''

# Контроль за вкл/выкл GIL осуществлялся через терминал
# Посредством обращения к виртуальному окружению ($env:PYTHON_GIL=0, python Comparison_2_with_4_gil_nogil.py)

def get_result_iter_2():
    if __name__ == "__main__":
        time1 = timeit.timeit(lambda: integrate_async_thread(math.cos, 0, math.pi / 2, n_jobs=2, n_iter=100), number=1)
        time2 = timeit.timeit(lambda: integrate_async_thread(math.cos, 0, math.pi / 2, n_jobs=4, n_iter=100), number=1)
        time3 = timeit.timeit(lambda: integrate_async_thread(math.cos, 0, math.pi / 2, n_jobs=6, n_iter=100), number=1)
        time4 = timeit.timeit(lambda: integrate_async_thread(math.cos, 0, math.pi / 2, n_jobs=8, n_iter=100), number=1)

        time5 = timeit.timeit(lambda: integrate_async_thread(math.sin, 0, math.pi, n_jobs=2, n_iter=100), number=1)
        time6 = timeit.timeit(lambda: integrate_async_thread(math.sin, 0, math.pi, n_jobs=4, n_iter=100), number=1)
        time7 = timeit.timeit(lambda: integrate_async_thread(math.sin, 0, math.pi, n_jobs=6, n_iter=100), number=1)
        time8 = timeit.timeit(lambda: integrate_async_thread(math.sin, 0, math.pi, n_jobs=8, n_iter=100), number=1)

        print(
            f"Время выполнения integrate_async_thread math.cos, 0 to pi/2, 2 threads, 100 iter, 1 compilation: {time1}")
        print(
            f"Время выполнения integrate_async_thread math.cos, 0 to pi/2, 4 threads, 100 iter, 1 compilation: {time2}")
        print(
            f"Время выполнения integrate_async_thread math.cos, 0 to pi/2, 6 threads, 100 iter, 1 compilation: {time3}")
        print(
            f"Время выполнения integrate_async_thread math.cos, 0 to pi/2, 8 threads, 100 iter, 1 compilation: {time4}")
        print("\n")
        print(
            f"Время выполнения integrate_async_thread math.sin, 0 to pi, 2 threads,  100 iter, 1 compilation: {time5}")
        print(
            f"Время выполнения integrate_async_thread math.sin, 0 to pi, 4 threads,  100 iter, 1 compilation: {time6}")
        print(
            f"Время выполнения integrate_async_thread math.sin, 0 to pi, 6 threads,  100 iter, 1 compilation: {time7}")
        print(
            f"Время выполнения integrate_async_thread math.sin, 0 to pi, 8 threads,  100 iter, 1 compilation: {time8}")
        print("\n")

def get_result_iter_4():
        time1_c = timeit.timeit(lambda: Integrate_optimized.integrate(math.cos, 0, math.pi / 2, n_iter=100), number=100)
        time2_c = timeit.timeit(lambda: Integrate_optimized.integrate(math.sin, 0, math.pi, n_iter=100), number=100)
        print(f"Время выполнения integrate_cython math.cos, 0 to pi/2, 100 iter: {time1_c}")
        print(f"Время выполнения integrate_cython math.sin, 0 to pi, 100 iter: {time2_c}")

        return 0


if __name__ == '__main__':
    print('Время выполнения Итерации 2:')
    get_result_iter_2()
    print('Время выполнения Итерации 4:')
    get_result_iter_4()

# GIL

# Время выполнения integrate_async_thread math.cos, 0 to pi/2, 2 threads, 100 iter, 1 compilation: 0.0036145001649856567
# Время выполнения integrate_async_thread math.cos, 0 to pi/2, 4 threads, 100 iter, 1 compilation: 0.0009574000723659992
# Время выполнения integrate_async_thread math.cos, 0 to pi/2, 6 threads, 100 iter, 1 compilation: 0.0014508003368973732
# Время выполнения integrate_async_thread math.cos, 0 to pi/2, 8 threads, 100 iter, 1 compilation: 0.0016240999102592468


# Время выполнения integrate_async_thread math.sin, 0 to pi, 2 threads,  100 iter, 1 compilation: 0.0009807003661990166
# Время выполнения integrate_async_thread math.sin, 0 to pi, 4 threads,  100 iter, 1 compilation: 0.0006730002351105213
# Время выполнения integrate_async_thread math.sin, 0 to pi, 6 threads,  100 iter, 1 compilation: 0.001015199813991785
# Время выполнения integrate_async_thread math.sin, 0 to pi, 8 threads,  100 iter, 1 compilation: 0.0011192001402378082


# Время выполнения integrate_cython math.cos, 0 to pi/2, 100 iter: 0.0007658000104129314
# Время выполнения integrate_cython math.sin, 0 to pi, 100 iter: 0.000771199818700552


# noGIL

# Время выполнения integrate_async_thread math.cos, 0 to pi/2, 2 threads, 100 iter, 1 compilation: 0.0036871000193059444
# Время выполнения integrate_async_thread math.cos, 0 to pi/2, 4 threads, 100 iter, 1 compilation: 0.0007703998126089573
# Время выполнения integrate_async_thread math.cos, 0 to pi/2, 6 threads, 100 iter, 1 compilation: 0.0008395998738706112
# Время выполнения integrate_async_thread math.cos, 0 to pi/2, 8 threads, 100 iter, 1 compilation: 0.0007043997757136822


# Время выполнения integrate_async_thread math.sin, 0 to pi, 2 threads,  100 iter, 1 compilation: 0.0004560002125799656
# Время выполнения integrate_async_thread math.sin, 0 to pi, 4 threads,  100 iter, 1 compilation: 0.00030110031366348267
# Время выполнения integrate_async_thread math.sin, 0 to pi, 6 threads,  100 iter, 1 compilation: 0.00035380013287067413
# Время выполнения integrate_async_thread math.sin, 0 to pi, 8 threads,  100 iter, 1 compilation: 0.0003475998528301716


# Время выполнения integrate_cython math.cos, 0 to pi/2, 100 iter: 0.0013578999787569046
# Время выполнения integrate_cython math.sin, 0 to pi, 100 iter: 0.0011494001373648643