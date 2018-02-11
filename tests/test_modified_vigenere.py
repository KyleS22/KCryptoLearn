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
