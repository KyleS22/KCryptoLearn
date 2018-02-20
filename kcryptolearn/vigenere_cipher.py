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

# TODO: Algorithm for breaking using Kasiski examination
    # TODO: 1. Find repeat sequence spacing -> Find every repeated set of letters at least three letters long
    # TODO: 2.1 Count spacing between each set of repeated charcters -> Ex. ABCeroiweurABCdflkjhsdfXYZslakdjXYZalksjdABC
    # TODO:                                                            between the first ABC and second ABC there are 11
    # TODO:                                                            between first and third ABC ...
    # TODO:                                                            between second and third ABC ...
    # TODO:                                                            between XYZ and second XYZ ... DONE
    # TODO: 2.2 Get factors of all the spacings found in 2.1
    # TODO: 2.3 Count how many times each factor appears
    # TODO: 2.4 The more times a factor appears, the more likely it is to be the keylength
    # TODO: 2.5 Split the text into k strings of every kth letter of the ciphertext where k is the keylength from 2.4
    # TODO: 3. Frequency analysis
    # TODO: 3.1 Decrypt ONE string obtained in 2.5 with every letter of the alphabet as the key (ie 26 decrypts for each
    # TODO:                                                                                                string)
    # TODO: 3.2 do english frequency analysis using index of coincidence on each decrypted string from 3.1
    # TODO: choose the decryptions closest to english, the letter used for these are the possible letters of the
    # TODO: key at the index of the string chosen in 3.1
    # TODO: Repeat 3.1 - 3.2 for each of the k strings to build up possible characters for each position of the key
    # TODO: Make all combinations of the characters chosen above and brute force decode through all combinations for the key