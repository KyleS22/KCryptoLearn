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

        #Calculate index of coincidence for each sub-string
        cur_index = 0
        for string in strings:
            ind_cos[cur_index] = ec.index_of_coincidence(string)
            cur_index += 1

        # Get the average index and see if it is close to english
        avg_index = sum(ind_cos)/len(ind_cos)

        if avg_index >= tolerance:
            return k, strings

    return -1, None


def get_largest_mutual_inidces_of_coincidence(strings, tolerance=0.065):
    """
    Returns a list of mutual indices of coincidence greater than a tolerance for each string compared to
    each other string
    :param strings: The list of strings to compare
    :param tolerance: The threshold for accepting mutual indices of coincidence
    :return: A dataframe (i -> the string block, j -> The next string block, shift-> the amount j was shifted,
     mutial_ind_co -> The mutual index of coincidence for this comparison)
    """

    column_nums = [x for x in range(26)]
    column_names = ['i', 'j'] + column_nums

    mutual_ind_cos = pd.DataFrame(columns=column_names)

    row_num = -1

    for block_i in range(len(strings) - 1):
        for block_j in range(block_i + 1, len(strings)):
            row_num += 1
            for shift_amount in range(26):
                shifted_string = []
                for char in strings[block_j]:
                    char_as_num = ec.convert_alpha_to_num(char)
                    shifted_char = (char_as_num + shift_amount) % 26
                    shifted_string.append(ec.convert_num_to_alpha(shifted_char))

                mutual_ind_cos.at[row_num, 'i'] = block_i
                mutual_ind_cos.at[row_num, 'j'] = block_j
                mutual_ind_cos.at[row_num, shift_amount] = ec.mutual_index_of_coincidence(strings[block_i],
                                                                                          str(shifted_string))

    rows = mutual_ind_cos.index
    columns = mutual_ind_cos.columns
    columns = columns[2:]

    largest_values = []


    for k in rows:
        for l in columns:
            if mutual_ind_cos[l][k] > tolerance:
                i = mutual_ind_cos['i'][k]
                j = mutual_ind_cos['j'][k]
                shift = l
                ind_co = mutual_ind_cos[l][k]
                largest_values.append([i, j, shift, ind_co])

    largest_values_df = pd.DataFrame(largest_values, columns=['i', 'j', 'shift', 'mut_ind_co'])
    return largest_values_df