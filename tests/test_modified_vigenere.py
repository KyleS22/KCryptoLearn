from unittest import TestCase
import kcryptolearn.modified_vigenere as MV
class TestModifiedVigenere(TestCase):

    def test_encode(self):
        encoded = MV.encode("ATTACKATDAWN", "JAZZ")

        answer = ['J','T', 'S', 'Z', 'U', 'D', 'R', 'R', 'G', 'D', 'M', 'D']

        self.assertEqual(encoded, answer, "Encoding incorrect.")
