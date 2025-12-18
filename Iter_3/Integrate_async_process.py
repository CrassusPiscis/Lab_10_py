import concurrent.futures as ftres
from functools import partial
from Integrate import integrate
def integrate_async_process(f, a, b, *, n_jobs=2, n_iter=1000):
    """
        Функция асинхронного интегрирования

        f: интегриируемая функция
        a: начальное значение x интервала интегрирования
        b: конечное значение x интервала интегрирования
        n_jobs: количество потоков
        n_iter:количество проводимых итераций вычислений площади под функцией в определенной точке

        :return: float: Возвращает интеграл функции исходя из заданных параметров
    """

    executor = ftres.ProcessPoolExecutor(max_workers=n_jobs) # создаваемый пул тредов будет размера n_jobs

    spawn = partial(executor.submit, integrate, f, n_iter = n_iter // n_jobs)   # partial позволяет "закрепить"
                                                                                # несколько аргументов
                                                                                # для удобства вызова функции ,
                                                                                # см. пример ниже
    step = (b - a) / n_jobs


    fs = [spawn(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]    # создаем потоки с помощью генератора
                                                                             # списков; partial позволил нам

    return sum(list(f.result() for f in ftres.as_completed(fs)))                     # as.completed() берет на вход список
                                                                                # фьючерсов и как только какой-то
                                                                                # завершился, возвращает результат
                                                                                # f.result(), далее, мы эти результаты
                                                                                # складываем
