from unittest import TestCase
import kcryptolearn.modified_vigenere as mv
class TestModifiedVigenere(TestCase):

    def test_encode(self):
        encoded = mv.encode("ATTACKATDAWN", "JAZZ")

        answer = ['J','T', 'S', 'Z', 'U', 'D', 'R', 'R', 'G', 'D', 'M', 'D']

        self.assertEqual(encoded, answer, "Encoding incorrect.")

    def test_decode(self):
        decoded = mv.decode("JTSZUDRRGDMD", "JAZZ")

        answer = ['A', 'T', 'T', 'A', 'C', 'K', 'A', 'T', 'D', 'A', 'W', 'N']

        self.assertEqual(decoded, answer, "Decoding incorrect.")


    def test_get_key_length(self):
        string = ['C', 'H', 'D', 'P', 'F', 'P', 'E', 'Y', 'P', 'G', 'R', 'T', 'L', 'L', 'E', 'P', 'D', 'F', 'P', 'D',
                  'E', 'T', 'J', 'G', 'E', 'M', 'P', 'J', 'Y', 'M', 'N', 'G', 'K', 'A', 'S']

        keylen_ans = 4   # Used key JAZZ

        keylen = mv.get_key_length(string)

        self.assertEqual(0, keylen % keylen_ans, "Wrong keylength.")
