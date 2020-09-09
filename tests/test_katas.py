import katas
import unittest
import math


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(10, 5), 15)
        self.assertEqual(katas.add(10, 90), 100)
        self.assertEqual(katas.add(-5, 10), 5)

    def test_multiply(self):
        self.assertEqual(katas.multiply(2, 8), 16)

    def test_power(self):
        self.assertEqual(katas.power(2, 2), 4)

    def test_factorial(self):
        self.assertIsNotNone(katas.factorial)
        self.assertEqual(katas.factorial(4), math.factorial(4))
        for x in range(10):
            self.assertEqual(katas.factorial(x), math.factorial(x))

    def test_fibonacci(self):

        self.assertEqual(katas.fibonacci(8), 13)


if __name__ == '__main__':
    unittest.main()
