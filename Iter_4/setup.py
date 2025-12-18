from setuptools import setup
from Cython.Build import cythonize

setup(
    name="Integrate_optimized",
    ext_modules=cythonize("Integrate_optimized.pyx", annotate=True),
)