"""


Author: Kyle Seidenthal
"""
from sympy import sieve


class QuadraticSieve:

    def get_factor_base(self, B):
        """
        Returns a list of primes less than B
        :param B: The smoothness bound
        :return: The primes less than B
        """
        return [p for p in sieve.primerange(2, B)]

    def relation_function(self, T,  N):
        """
        Returns the value of the function T^2 - N
        :param T: The input to the function
        :param N: The value to use for N
        :return: T^2 - N
        """
        return T**2 - N



