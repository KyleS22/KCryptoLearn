"""
Implementation of the Vigenere Cipher

Author: Kyle Seidenthal
"""
import kcryptolearn.english_crypto as ec
import pandas as pd
import numpy as np


def encode(msg, key):
    """
    Encode a message using the vigenere cipher
    :param msg: The message to encode
    :param key: The key to use for encryption
    :return: The encoded text
    """
    msg_nums = ec.convert_alpha_to_nums(msg)
    key_nums = ec.convert_alpha_to_nums(key)

    key_index = 0

    encoded_string = []

    for char in msg_nums:
        encoded_string.append((char + key_nums[key_index]) % 26)

        key_index = (key_index + 1) % len(key)

    return ec.convert_nums_to_alpha(encoded_string)


def decode(msg, key):
    """
    Decode a message using the vigenere cipher
    :param msg: The message to decode
    :param key: The key to use for decryption
    :return: The decoded text
    """
    msg_nums = ec.convert_alpha_to_nums(msg)
    key_nums = ec.convert_alpha_to_nums(key)

    key_index = 0

    encoded_string = []

    for char in msg_nums:
        encoded_string.append((char - key_nums[key_index]) % 26)

        key_index = (key_index + 1) % len(key)

    return ec.convert_nums_to_alpha(encoded_string)


def guess_keylen(msg, tolerance=0.06):
    """
    Guess the keylength for the message using index of coincidence
    :param msg: The message to get the keylength for
    :return: The proposed keylength, a list of strings of the text divided into k groups k characters apart
    """
    # Try every key length until we find a good one
    for k in range(1, len(msg)):
        strings = [""] * k

        # Split the text into k strings of every kth letter
        for i in range(len(msg)):
            strings[i % k] += msg[i]

        ind_cos = [0] * k

        # Calculate index of coincidence for each sub-string
        cur_index = 0
        for string in strings:
            ind_cos[cur_index] = ec.index_of_coincidence(string)
            cur_index += 1

        # Get the average index and see if it is close to english
        avg_index = sum(ind_cos) / len(ind_cos)

        if avg_index >= tolerance:
            return k, strings

    return -1, None


def split_into_k_strings(msg, k):
    """
    Split a string into k strings.  Each string will have every kth letter from the start character

    ex.
    s = ABCDEFGHI, k = 3

    s1 = ADG
    s2 = BEH
    s3 = CFI

    :param msg: The message to split into k strings
    :param k: The number of strings to split msg into
    :return: A list of strings split into k strings
    """
    # Make sure there are no spaces
    msg = msg.replace(" ", "")

    # Make a list of k strings
    strings = [""] * k

    for i in range(len(msg)):
        strings[i % k] += msg[i]

    return strings


def shift_string_by_n(string, n):
    """
    Given a string, shift the characters up by n
    :param string: The string to shift
    :param n: The amount to shift each character by
    :return: The shifted string
    """
    string_nums = ec.convert_alpha_to_nums(string)

    shifted = []

    for char in string_nums:
        shifted.append((char + n) % 26)

    return ec.convert_nums_to_alpha(shifted)


def get_all_mutual_indices_of_coincidence(strings):
    """
    Get a dataframe of all mutual indices of coincidence for a set of strings for each possible shift
    amount of each string

    :param strings: A list of strings to get the indices of coincidence for
    :return: A pandas dataframe of all mutual indices of coincidence
    """
    # Set up the columns of the data frame, 0-25, one column for each shift
    column_nums = [x for x in range(26)]
    column_names = ['i', 'j'] + column_nums  # Add a column to keep track of which string the index to belongs to

    mutual_ind_cos = pd.DataFrame(columns=column_names)

    row_num = -1

    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            row_num += 1
            for shift_amount in range(26):
                shifted_string = shift_string_by_n(strings[j], shift_amount)

                ind_co = ec.mutual_index_of_coincidence(strings[i], ''.join(shifted_string))

                mutual_ind_cos.at[row_num, 'i'] = i
                mutual_ind_cos.at[row_num, 'j'] = j
                mutual_ind_cos.at[row_num, shift_amount] = ind_co

    return mutual_ind_cos


def get_largest_mutual_indices_of_coincidence(all_ind_cos, tolerance=0.064):
    """
    Given a dataframe of all mutual indices of coincidence, find all indices greater than tolerance
    :param all_ind_cos: A pandas dataframe of all indices of coincidence for a set of strings
    :param tolerance: The lowest an index of coincidence can be to be included
    :return: A datframe containing the highest mutual indices of coincidence and the string numbers they belong to
    """
    rows = all_ind_cos.index
    columns = all_ind_cos.columns
    columns = columns[2:]

    largest_values = []

    for k in rows:
        for l in columns:
            if all_ind_cos[l][k] > tolerance:
                i = all_ind_cos['i'][k]
                j = all_ind_cos['j'][k]
                shift = l
                ind_co = all_ind_cos[l][k]
                largest_values.append([i, j, shift, ind_co])

    largest_values_df = pd.DataFrame(largest_values, columns=['i', 'j', 'shift', 'mut_ind_co'])
    return largest_values_df


def get_avg_indices_of_coincidence(strings):
    """
    Get the average of the indices of coincidence for a set of strings
    :param strings: The set of strings to find the indices of coincidence for
    :return: The average index of coincidence
    """
    ind_cos = []

    for string in strings:
        ind_co = ec.index_of_coincidence(string)
        ind_cos.append(ind_co)

    avg_ind_co = sum(ind_cos) / len(ind_cos)

    return avg_ind_co


def generate_all_possible_keys(largest_indices_of_coincidence):
    """
    Gets a list of all possible keys by solving the linear equation provided by the largest indices of coincidence.
    :param largest_indices_of_coincidence: A pandas dataframe with the largest indices of coincidence and their shift
            amounts
    :return: A list of keys to try
    """

    return []

def break_vigenere_cipher(msg):
    """
    Decode the given message.  Only effective with long strings of text.  Will output a large number of possible
    decryptions to choose from.
    :param msg: The encrypted text
    :return: A list of possible decrytions
    """

    return None