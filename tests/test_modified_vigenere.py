import unittest
import kcryptolearn.modified_vigenere as mv
import kcryptolearn.english_crypto as ec
import kcryptolearn.vigenere_cipher as vc

class TestModifiedVigenere(unittest.TestCase):

    def test_encode(self):
        encoded = mv.encode("ATTACKATDAWN", "JAZZ")

        answer = ['J','T', 'S', 'Z', 'U', 'D', 'R', 'R', 'G', 'D', 'M', 'D']

        self.assertEqual(encoded, answer, "Encoding incorrect.")

    def test_decode(self):
        decoded = mv.decode("JTSZUDRRGDMD", "JAZZ")

        answer = ['A', 'T', 'T', 'A', 'C', 'K', 'A', 'T', 'D', 'A', 'W', 'N']

        self.assertEqual(decoded, answer, "Decoding incorrect.")

    def test_reduce_to_normal_vigenere(self):
        string = "ATTACKATDAWN"
        encoded_string = mv.encode(string, "JAZZ")

        vigenere_text = mv.reduce_to_regular_vigenere(encoded_string, 4)
        vigenere_text = ec.convert_alpha_to_nums(vigenere_text)

        actual_vegenere_text = [9, 19, 18, 25, 11, 10, 25, 18, 12, 0, 21, 12]

        self.assertEqual(actual_vegenere_text, vigenere_text, "The cipher texts to not match")

    def test_break_modified_vigenere(self):
        key = "Test"
        string = "Today is a good day to go outside and play.  Wouldn't you agree?  This string needs to be long for " \
                 "vigenere to be useful"

        encoded_text = mv.encode(string, key)

        possible_decoded = mv.break_modified_vigenere(encoded_text)

        actual_possible_decoded = []

        for i in range(26):
            shifted_key = vc.shift_string_by_n(key, i)
            actual_possible_decoded.append(vc.encode(string, shifted_key))

        self.assertListEqual(possible_decoded, actual_possible_decoded, "Decoded possiblilities are incorrect.")