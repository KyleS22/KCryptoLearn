"""
Tests for English Cryptography functions

Author: Kyle Seidenthal
"""
from unittest import TestCase
import kcryptolearn.english_crypto as ec

class TestEnglishCrypto(TestCase):

    def test_convert_alpha_to_nums(self):

        numbers = ec.convert_alpha_to_nums("hello")

        answer = [7, 4, 11, 11, 14]

        self.assertEqual(numbers, answer, "Conversion to numbers failed")

        numbers = ec.convert_alpha_to_nums("HELLO")

        answer = [7, 4, 11, 11, 14]

        self.assertEqual(numbers, answer, "Conversion to numbers failed")

        numbers = ec.convert_alpha_to_nums(1)

        answer = [7, 4, 11, 11, 14]

        self.assertRaises(Exception)

        numbers = ec.convert_alpha_to_nums("potato")

        answer = [15, 14, 19, 0, 19, 14]

        self.assertEqual(numbers, answer, "Conversion to numbers failed")

        numbers = ec.convert_alpha_to_nums("pot ato")

        answer = [15, 14, 19, 0, 19, 14]

        self.assertEqual(numbers, answer, "Conversion to numbers failed")


    def test_convert_nums_to_alpha(self):
        alpha = ec.convert_nums_to_alpha([7, 4, 11, 11, 14])

        answer = ['H', 'E', 'L', 'L', 'O']

        self.assertEqual(alpha, answer, "Conversion to alpha failed")

        alpha = ec.convert_nums_to_alpha([15, 14, 19, 0, 19, 14])

        answer = ['P', 'O', 'T', 'A', 'T', 'O']

        self.assertEqual(alpha, answer, "Conversion to alpha failed")



    def test_convert_num_to_alpha(self):
        num = ec.convert_num_to_alpha(5)
        answer = 'F'

        self.assertEqual(num, answer, "Invalid num to alpha conversion")

        num = ec.convert_num_to_alpha(7)
        answer = 'H'

        self.assertEqual(num, answer, "Invalid num to alpha conversion")


    def test_convert_alpha_to_num(self):
        alpha = ec.convert_alpha_to_num("A")
        answer = 0

        self.assertEqual(alpha, answer, "Invalid alpha to num conversion.")

        alpha = ec.convert_alpha_to_num("Z")
        answer = 25

        self.assertEqual(alpha, answer, "Invalid alpha to num conversion.")


    def test_get_frequency_count(self):
        string = "AAAAB"
        freq = ec.get_frequency_count(string)

        answer = {"A": 4, "B": 1}

        self.assertDictEqual(freq, answer)

        string = "The Quick Brown Fox Jumps Over The Lazy Dog"
        freq = ec.get_frequency_count(string)

        answer = {"A": 1, "B": 1, "C": 1, "D": 1, "E": 3, "F": 1, "G": 1, "H": 2, "I": 1, "J": 1, "K": 1, "L": 1, "M": 1,
                  "N": 1,"O": 4, "P": 1, "Q": 1, "R": 2, "S": 1, "T": 2, "U": 2, "V": 1, "W": 1, "X": 1, "Y":1, "Z": 1 }

        self.assertDictEqual(freq, answer)

    def test_index_of_coincidence(self):
        string = "A BIRD IN HAND IS WORTH TWO IN THE BUSH"
        actual_index = 0.0575

        index = ec.index_of_coincidence(string)

        self.assertAlmostEqual(actual_index, index, places=4)

