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
