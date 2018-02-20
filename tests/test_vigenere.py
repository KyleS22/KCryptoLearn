"""


Author: Kyle Seidenthal
"""
import unittest
import kcryptolearn.vigenere_cipher as vc
import kcryptolearn.english_crypto as ec


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


