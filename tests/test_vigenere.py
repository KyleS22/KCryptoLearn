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
        # TODO: This can be improved
        keylen, strings = vc.guess_keylen(['Y', 'S', 'E', 'D', 'I', 'V', 'T', 'W', 'S', 'D','P', 'M', 'Q', 'A', 'Y', 'H', 'F',
                                  'J', 'S', 'Y', 'I', 'V', 'T', 'Z', 'D', 'T', 'N', 'F', 'P', 'R', 'V', 'Z', 'F', 'T',
                                  'N'])
        actual_keylen = 8

        self.assertEqual(keylen, actual_keylen, "Wrong keylength.")


    def test_get_largest_mutual_indices_of_coincidence(self):
        self.fail()

    def test_split_into_k_strings(self):
        self.fail()

    def test_shift_string_by_n(self):
        self.fail()

    def test_get_all_mutual_indices_of_coincidence(self):
        self.fail()

    def test_get_average_indices_of_coincidence(self):
        self.fail()



