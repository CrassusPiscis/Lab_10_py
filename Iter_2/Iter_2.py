import math
import timeit
from Integrate_async_thread import integrate_async_thread

def get_result():
    if __name__ == "__main__":
        time1 = timeit.timeit(lambda: integrate_async_thread(math.cos, 0, math.pi / 2, n_jobs=2, n_iter=100),  number=1)
        time2 = timeit.timeit(lambda: integrate_async_thread(math.cos, 0, math.pi / 2, n_jobs=4, n_iter=100), number=1)
        time3 = timeit.timeit(lambda: integrate_async_thread(math.cos, 0, math.pi / 2, n_jobs=6, n_iter=100), number=1)
        time4 = timeit.timeit(lambda: integrate_async_thread(math.cos, 0, math.pi / 2, n_jobs=8, n_iter=100), number=1)

        time5 = timeit.timeit(lambda: integrate_async_thread(math.sin, 0, math.pi, n_jobs=2, n_iter=100), number=1)
        time6 = timeit.timeit(lambda: integrate_async_thread(math.sin, 0, math.pi, n_jobs=4, n_iter=100), number=1)
        time7 = timeit.timeit(lambda: integrate_async_thread(math.sin, 0, math.pi, n_jobs=6, n_iter=100), number=1)
        time8 = timeit.timeit(lambda: integrate_async_thread(math.sin, 0, math.pi, n_jobs=8, n_iter=100), number=1)

        print(f"Время выполнения integrate_async_thread math.cos, 0 to pi/2, 2 threads, 100 iter, 1 compilation: {time1}")
        print(f"Время выполнения integrate_async_thread math.cos, 0 to pi/2, 4 threads, 100 iter, 1 compilation: {time2}")
        print(f"Время выполнения integrate_async_thread math.cos, 0 to pi/2, 6 threads, 100 iter, 1 compilation: {time3}")
        print(f"Время выполнения integrate_async_thread math.cos, 0 to pi/2, 8 threads, 100 iter, 1 compilation: {time4}")
        print("\n")
        print(f"Время выполнения integrate_async_thread math.sin, 0 to pi, 2 threads,  100 iter, 1 compilation: {time5}")
        print(f"Время выполнения integrate_async_thread math.sin, 0 to pi, 4 threads,  100 iter, 1 compilation: {time6}")
        print(f"Время выполнения integrate_async_thread math.sin, 0 to pi, 6 threads,  100 iter, 1 compilation: {time7}")
        print(f"Время выполнения integrate_async_thread math.sin, 0 to pi, 8 threads,  100 iter, 1 compilation: {time8}")

        return [time1, time2, time3, time4, time5, time6, time7, time8]