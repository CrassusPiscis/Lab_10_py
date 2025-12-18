from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("Inter_nogil_threads.pyx")
)