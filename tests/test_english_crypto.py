"""
Tests for English Cryptography functions

Author: Kyle Seidenthal
"""
from unittest import TestCase
import kcryptolearn.english_crypto as EC

class TestEnglishCrypto(TestCase):

    def test_convert_alpha_to_nums(self):

        numbers = EC.convert_alpha_to_nums("hello")

        answer = [7, 4, 11, 11, 14]

        self.assertEqual(numbers, answer, "Conversion to numbers failed")

        numbers = EC.convert_alpha_to_nums("HELLO")

        answer = [7, 4, 11, 11, 14]

        self.assertEqual(numbers, answer, "Conversion to numbers failed")

        numbers = EC.convert_alpha_to_nums(1)

        answer = [7, 4, 11, 11, 14]

        self.assertRaises(Exception)

        numbers = EC.convert_alpha_to_nums("potato")

        answer = [15, 14, 19, 0, 19, 14]

        self.assertEqual(numbers, answer, "Conversion to numbers failed")



    def test_convert_nums_to_alpha(self):
        alpha = EC.convert_nums_to_alpha([7, 4, 11, 11, 14])

        answer = ['H', 'E', 'L', 'L', 'O']

        self.assertEqual(alpha, answer, "Conversion to alpha failed")

        alpha = EC.convert_nums_to_alpha([15, 14, 19, 0, 19, 14])

        answer = ['P', 'O', 'T', 'A', 'T', 'O']

        self.assertEqual(alpha, answer, "Conversion to alpha failed")



    def test_convert_num_to_alpha(self):
        num = EC.convert_num_to_alpha(5)
        answer = 'F'

        self.assertEqual(num, answer, "Invalid num to alpha conversion")

        num = EC.convert_num_to_alpha(7)
        answer = 'H'

        self.assertEqual(num, answer, "Invalid num to alpha conversion")


    def test_convert_alpha_to_num(self):
        alpha = EC.convert_alpha_to_num("A")
        answer = 0

        self.assertEqual(alpha, answer, "Invalid alpha to num conversion.")

        alpha = EC.convert_alpha_to_num("Z")
        answer = 25

        self.assertEqual(alpha, answer, "Invalid alpha to num conversion.")
