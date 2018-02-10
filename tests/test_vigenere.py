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

    def test_guess_keylen(self):
        # A hand crafted example
        keylen, strings = vc.guess_keylen(['Y', 'S', 'E', 'D', 'I', 'V', 'T', 'W', 'S', 'D','P', 'M', 'Q', 'A', 'Y', 'H', 'F',
                                  'J', 'S', 'Y', 'I', 'V', 'T', 'Z', 'D', 'T', 'N', 'F', 'P', 'R', 'V', 'Z', 'F', 'T',
                                  'N'])
        actual_keylen = 8

        self.assertEqual(keylen, actual_keylen, "Wrong keylength.")

        key = "Test"
        string = "Today is a good day to go outside and play.  Wouldn't you agree?  This string needs to be long for " \
                 "vigenere to be useful"

        encoded_text = vc.encode(string, key)

        keylen, strings = vc.guess_keylen(encoded_text)

        self.assertEqual(keylen, len(key), "Wrong keylength")

    def test_get_all_mutual_indices_of_coincidence(self):
        string1 = "Hello how are you"
        string2 = "This is another string"
        string3 = "One more string"

        mut_ind_cos = vc.get_all_mutual_indices_of_coincidence([string1, string2, string3])

        mut_ind_cos_list = mut_ind_cos.values.tolist()

        ans_row1 = [0, 1, 0.045112781954887216, 0.041353383458646614, 0.011278195488721804, 0.05263157894736842,
                    0.041353383458646614, 0.02631578947368421, 0.04887218045112782, 0.06390977443609022,
                    0.02631578947368421, 0.02631578947368421, 0.022556390977443608, 0.041353383458646614,
                    0.03759398496240601, 0.03383458646616541, 0.04887218045112782, 0.03007518796992481,
                    0.041353383458646614, 0.02631578947368421, 0.041353383458646614, 0.03759398496240601,
                    0.041353383458646614, 0.03383458646616541, 0.06390977443609022, 0.045112781954887216,
                    0.03759398496240601, 0.03383458646616541]

        ans_row2 = [0, 2, 0.06593406593406594, 0.049450549450549455, 0.02197802197802198, 0.06043956043956045,
                    0.016483516483516484, 0.03296703296703297, 0.03296703296703297, 0.049450549450549455,
                    0.038461538461538464, 0.027472527472527476, 0.049450549450549455, 0.027472527472527476,
                    0.03296703296703297, 0.04395604395604396, 0.027472527472527476, 0.01098901098901099,
                    0.06593406593406594, 0.02197802197802198, 0.04395604395604396, 0.03296703296703297,
                    0.06043956043956045, 0.027472527472527476, 0.038461538461538464, 0.05494505494505495,
                    0.038461538461538464, 0.027472527472527476]

        ans_row3 = [1, 2, 0.08906882591093118, 0.06072874493927126, 0.048582995951417005, 0.032388663967611336,
                    0.06477732793522267, 0.06477732793522267, 0.04048582995951417, 0.024291497975708502,
                    0.008097165991902834, 0.032388663967611336, 0.020242914979757085, 0.024291497975708502,
                    0.024291497975708502, 0.048582995951417005, 0.04048582995951417, 0.05263157894736842,
                    0.03643724696356275, 0.032388663967611336, 0.016194331983805668, 0.024291497975708502,
                    0.05668016194331984, 0.04453441295546559, 0.04453441295546559, 0.008097165991902834,
                    0.016194331983805668, 0.04453441295546559]

        self.assertEqual(ans_row1, mut_ind_cos_list[0], "The row is incorrect")
        self.assertEqual(ans_row2, mut_ind_cos_list[1], "The row is incorrect")
        self.assertEqual(ans_row3, mut_ind_cos_list[2], "The row is incorrect")

    def test_get_largest_mutual_indices_of_coincidence(self):
        string1 = "Hello how are you"
        string2 = "This is another string"
        string3 = "One more string"

        mut_ind_cos = vc.get_all_mutual_indices_of_coincidence([string1, string2, string3])

        largest = vc.get_largest_mutual_indices_of_coincidence(mut_ind_cos)

        largest_list = largest.values.tolist()

        row1 = [0.0, 2.0, 0.0, 0.06593406593406594]
        row2 = [0.0, 2.0, 16.0, 0.06593406593406594]
        row3 = [1.0, 2.0, 0.0, 0.08906882591093118]
        row4 = [1.0, 2.0, 4.0, 0.06477732793522267]
        row5 = [1.0, 2.0, 5.0, 0.06477732793522267]

        self.assertEqual(row1, largest_list[0], "The row is incorrect")
        self.assertEqual(row2, largest_list[1], "The row is incorrect")
        self.assertEqual(row3, largest_list[2], "The row is incorrect")
        self.assertEqual(row4, largest_list[3], "The row is incorrect")
        self.assertEqual(row5, largest_list[4], "The row is incorrect")


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
        string = "A BIRD IN HAND IS WORTH TWO IN THE BUSH"
        actual_index1 = ec.index_of_coincidence(string)

        string2 = "This is a test"
        actual_index2 = ec.index_of_coincidence(string2)

        avgs = [actual_index1, actual_index2]
        actual_avg = sum(avgs)/len(avgs)

        computed_avg = vc.get_avg_indices_of_coincidence([string, string2])
        self.assertAlmostEqual(actual_avg, computed_avg, places=4)



