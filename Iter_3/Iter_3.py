import math
import timeit
from Integrate_async_process import integrate_async_process

'''
Было уменьшено количество повторение в timeit, так как выполнение 
уже одной операции многопроцессного вычисления занимает много времени
(примерно 0.2 секунды)
'''

def get_result():
    if __name__ == '__main__':
        time1 = timeit.timeit(lambda: integrate_async_process(math.cos, 0, math.pi / 2, n_jobs=2, n_iter=100), number=1)
        time2 = timeit.timeit(lambda: integrate_async_process(math.cos, 0, math.pi / 2, n_jobs=4, n_iter=100), number=1)
        time3 = timeit.timeit(lambda: integrate_async_process(math.cos, 0, math.pi / 2, n_jobs=6, n_iter=100), number=1)
        time4 = timeit.timeit(lambda: integrate_async_process(math.cos, 0, math.pi / 2, n_jobs=8, n_iter=100), number=1)

        time5 = timeit.timeit(lambda: integrate_async_process(math.sin, 0, math.pi, n_jobs=2, n_iter=100), number=1)
        time6 = timeit.timeit(lambda: integrate_async_process(math.sin, 0, math.pi, n_jobs=4, n_iter=100), number=1)
        time7 = timeit.timeit(lambda: integrate_async_process(math.sin, 0, math.pi, n_jobs=6, n_iter=100), number=1)
        time8 = timeit.timeit(lambda: integrate_async_process(math.sin, 0, math.pi, n_jobs=8, n_iter=100), number=1)

        print(f"Время выполнения integrate_async_process math.cos, 0 to pi/2, 2 processes, 100 iter, 1 compilation: {time1}")
        print(f"Время выполнения integrate_async_process math.cos, 0 to pi/2, 4 processes, 100 iter, 1 compilation: {time2}")
        print(f"Время выполнения integrate_async_process math.cos, 0 to pi/2, 6 processes, 100 iter, 1 compilation: {time3}")
        print(f"Время выполнения integrate_async_process math.cos, 0 to pi/2, 8 processes, 100 iter, 1 compilation: {time4}")
        print("\n")
        print(f"Время выполнения integrate_async_process math.sin, 0 to pi, 2 processes,  100 iter, 1 compilation: {time5}")
        print(f"Время выполнения integrate_async_process math.sin, 0 to pi, 4 processes,  100 iter, 1 compilation: {time6}")
        print(f"Время выполнения integrate_async_process math.sin, 0 to pi, 6 processes,  100 iter, 1 compilation: {time7}")
        print(f"Время выполнения integrate_async_process math.sin, 0 to pi, 8 processes,  100 iter, 1 compilation: {time8}")

        return [time1, time2, time3, time4, time5, time6, time7, time8]