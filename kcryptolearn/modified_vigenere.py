"""
Implementation of the Modified Vigenere Cipher

Author: Kyle Seidenthal
"""
import kcryptolearn.english_crypto as ec
import math
import kcryptolearn.vigenere_cipher as vc

N = 26  # For english letter encoding

def encode(msg, key):
    """
    Encode an english message using a key with the Modified Vigenere Cipher
    :param msg: The message to encode
    :param key: The key to use to encode the message
    :return: The encoded message
    """
    # Convert messages to numbers
    msg_nums = ec.convert_alpha_to_nums(msg)
    key_nums = ec.convert_alpha_to_nums(key)

    # Store the key length
    n = len(key)

    # A place to store the encoded message
    encoded_msg = []

    # We need to keep track of where we are in the key and message
    cur_msg_index = 0
    cur_key_index = 0

    # While there are still message numbers to encode...
    while cur_msg_index < len(msg_nums):
            encoded_num = (msg_nums[cur_msg_index] + key_nums[cur_key_index]) % N   # Add the message number to the key
            cur_key_index = (cur_key_index + 1) % n     # Update the key index

            # If we have encoded n or more numbers
            if cur_msg_index >= n:
                # Also use the previous encoded characters to encode the message
                encoded_num += (encoded_msg[(cur_msg_index - n)]) % N

            encoded_msg.append(encoded_num)
            cur_msg_index += 1

    encoded_string = ec.convert_nums_to_alpha(encoded_msg)

    return encoded_string

def decode(msg, key):
    """
    Decode a message given a key using the modified vigenere cipher
    :param msg: The message to decode
    :param key: The key to use
    :return: The decoded message
    """
    # Convert messages to numbers
    msg_nums = ec.convert_alpha_to_nums(msg)
    key_nums = ec.convert_alpha_to_nums(key)

    # Store the key length
    n = len(key)

    decoded_msg = []

    # We need to keep track of where we are in the key and message
    cur_msg_index = 0
    cur_key_index = 0

    # While there are still message numbers to decode...
    while cur_msg_index < len(msg_nums):
        decoded_num = (msg_nums[cur_msg_index] - key_nums[cur_key_index]) % N   # Subtract the key from the ciphertext
        cur_key_index = (cur_key_index + 1) % n     # Update the key index

        # If we have decoded n or more numbers
        if cur_msg_index >= n:
            # Also subtract the previous encoded characters
            decoded_num -= (msg_nums[(cur_msg_index - n)]) % N

        decoded_msg.append(decoded_num)
        cur_msg_index += 1

    decoded_string = ec.convert_nums_to_alpha(decoded_msg)

    return decoded_string


def reduce_to_regular_vigenere(msg, keylen):
    """
    Given the keylength, turn the problem into a normal vigenere cipher problem
    :param msg: The encoded message
    :param keylen: The length of the key
    :return: The ciphertext as a vigenere cipher
    """
    msg_nums = ec.convert_alpha_to_nums(msg)

    cur_index = 0

    vigenere_text = []

    while cur_index < len(msg_nums):

        if cur_index < keylen:
            vigenere_text.append(msg_nums[cur_index])

        else:
            vigenere_text.append(msg_nums[cur_index] - msg_nums[cur_index - keylen])

        cur_index += 1


    return ec.convert_nums_to_alpha(vigenere_text)

def break_modified_vigenere(msg):
    """
    Decode the message by trying all keylengths k and reducing to a normal vigenere problem and guessing its keylength.
    If the keylength of the reduced problem cannot be found, try the next keylength
    :param msg: The message to decode
    :return: Possible decryptions.
    """

    return []

