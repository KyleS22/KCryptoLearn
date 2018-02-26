"""


Author: Kyle Seidenthal
"""
from unittest import TestCase
import kcryptolearn.quadratic_sieve as qs

class TestQuadraticSieve(TestCase):

    def test_get_factor_base(self):
        factor_base = qs.get_factor_base(10)
        expected = [2, 3, 5, 7]

        self.assertListEqual(factor_base, expected)