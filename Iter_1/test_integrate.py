from Integrate import *
import unittest
import math

class TestIntegrate(unittest.TestCase):

    def test_cos_integration(self):
        result = integrate(math.cos, 0, math.pi / 2, n_iter=1000)
        self.assertAlmostEqual(result, 1, delta=0.001)

    def test_sin_integration(self):
        result = integrate(math.sin, 0, math.pi)
        self.assertAlmostEqual(result, 2, delta=0.001)

    def test_integration_small_iter(self):
        result = integrate(math.sin, 0, math.pi, n_iter=100)
        self.assertTrue(1.9 < result < 2.1)

    def test_linear_function(self):
        result = integrate(lambda x: 5, 0, 3, n_iter=10)
        self.assertEqual(result, 15)

if __name__ == '__main__':
    unittest.main()
