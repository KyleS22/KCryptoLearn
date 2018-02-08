"""


Author: Kyle Seidenthal
"""
import unittest
import kcryptolearn.vigenere_cipher as vc


class TestVigenere(unittest.TestCase):
    def test_encode(self):
        encoded_string = vc.encode("The rain in spain stays mainly in the plain", "flamingo")
        actual_encoded_string = ['Y', 'S', 'E', 'D', 'I', 'V', 'T', 'W', 'S', 'D','P', 'M', 'Q', 'A', 'Y', 'H', 'F',
                                 'J', 'S', 'Y', 'I', 'V', 'T', 'Z', 'D', 'T', 'N', 'F', 'P', 'R', 'V', 'Z', 'F', 'T',
                                 'N']

        self.assertEqual(encoded_string, actual_encoded_string, "Encoding incorrect.")

    def test_decode(self):
        decoded_string = vc.decode(['Y', 'S', 'E', 'D', 'I', 'V', 'T', 'W', 'S', 'D','P', 'M', 'Q', 'A', 'Y', 'H', 'F',
                                    'J', 'S', 'Y', 'I', 'V', 'T', 'Z', 'D', 'T', 'N', 'F', 'P', 'R', 'V', 'Z', 'F', 'T',
                                    'N'], "flamingo")

        actual_decoded_string = ['T', 'H', 'E', 'R', 'A', 'I', 'N', 'I', 'N', 'S', 'P', 'A', 'I', 'N', 'S', 'T', 'A',
                                 'Y', 'S', 'M', 'A', 'I', 'N', 'L', 'Y', 'I', 'N', 'T', 'H', 'E', 'P', 'L', 'A', 'I',
                                 'N']

        self.assertEqual(decoded_string, actual_decoded_string, "Decoding incorrect.")

    def test_guess_keylen(self):
        keylen, strings = vc.guess_keylen(['Y', 'S', 'E', 'D', 'I', 'V', 'T', 'W', 'S', 'D','P', 'M', 'Q', 'A', 'Y', 'H', 'F',
                                  'J', 'S', 'Y', 'I', 'V', 'T', 'Z', 'D', 'T', 'N', 'F', 'P', 'R', 'V', 'Z', 'F', 'T',
                                  'N'])
        actual_keylen = 8

        self.assertEqual(keylen, actual_keylen, "Wrong keylength.")

    def test_get_all_mutual_indices_of_coincidence(self):
        self.fail()

    def test_get_largest_mutual_indices_of_coincidence(self):
        self.fail()

    def test_split_into_k_strings(self):
        string = "ThisIsATest"
        k = 3

        split_string = vc.split_into_k_strings(string, k)

        self.assertEqual(split_string[0], "TsAs", "String was not split correctly")
        self.assertEqual(split_string[1], "hITt", "String was not split correctly")
        self.assertEqual(split_string[2], "ise", "String was not split correctly")

        string = "Hello"
        k = 10

        split_string = vc.split_into_k_strings(string, k)

        self.assertEqual(split_string[0], "H", "String was not split correctly")
        self.assertEqual(split_string[1], "e", "String was not split correctly")
        self.assertEqual(split_string[2], "l", "String was not split correctly")
        self.assertEqual(split_string[3], "l", "String was not split correctly")
        self.assertEqual(split_string[4], "o", "String was not split correctly")

        string = "Hello How Are You Today"
        k = 6

        split_string = vc.split_into_k_strings(string, k)

        self.assertEqual(split_string[0], "Hooy", "String was not split correctly")
        self.assertEqual(split_string[1], "ewu", "String was not split correctly")
        self.assertEqual(split_string[2], "lAT", "String was not split correctly")
        self.assertEqual(split_string[3], "lro", "String was not split correctly")
        self.assertEqual(split_string[4], "oed", "String was not split correctly")
        self.assertEqual(split_string[5], "HYa", "String was not split correctly")

    def test_shift_string_by_n(self):
        string = "Hello"
        n = 1

        shifted_string = vc.shift_string_by_n(string, n)

        self.assertEqual(shifted_string, ['I', 'F', 'M', 'M', 'P'], "String was not shifted correctly")

        string = "This Is A Test"
        n = 5

        shifted_string = vc.shift_string_by_n(string, n)

        self.assertEqual(shifted_string, ['Y', 'M', 'N', 'X', 'N', 'X', 'F', 'Y', 'J', 'X', 'Y'], "String was not shifted correctly")


    def test_get_average_indices_of_coincidence(self):
        self.fail()



