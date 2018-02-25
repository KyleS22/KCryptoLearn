"""


Author: Kyle Seidenthal
"""
from unittest import TestCase
from kcryptolearn.quadratic_sieve import QuadraticSieve

class TestQuadraticSieve(TestCase):

    def test_get_factor_base(self):
        sieve = QuadraticSieve()
        factor_base = sieve.get_factor_base(10)
        expected = [2, 3, 5, 7]

        self.assertListEqual(factor_base, expected)