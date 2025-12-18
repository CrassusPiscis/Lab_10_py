import concurrent.futures as ftres
from functools import partial


# итерация 1
def integrate(f, a, b, *, n_iter=1000):
  """

    Функция интеграции заданной функции

    f: Функция, которая будет интегрироваться
    a: Начальная точка x функции для интегрирования
    b: Конечная точка x функции для интегрирования
    n: количество проводимых итераций вычисления площади под функцией в точке
  - замерить время вычисления функции (timeit), записать время
  вычисления
  """
  acc = 0
  step = (b - a) / n_iter
  for i in range(n_iter):
    acc += f(a + i*step) * step
  return acc


def integrate_async_thread(f, a, b, *, n_jobs=2, n_iter=1000):
    """
        Функция асинхронного интегрирования

        f: интегриируемая функция
        a: начальное значение x интервала интегрирования
        b: конечное значение x интервала интегрирования
        n_jobs: количество потоков
        n_iter:количество проводимых итераций вычислений площади под функцией в определенной точке

        :return: float: Возвращает интеграл функции исходя из заданных параметров
    """

    executor = ftres.ThreadPoolExecutor(max_workers=n_jobs) # создаваемый пул тредов будет размера n_jobs

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
