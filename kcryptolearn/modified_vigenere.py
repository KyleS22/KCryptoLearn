"""
Implementation of the Modified Vigenere Cipher

Author: Kyle Seidenthal
"""
import kcryptolearn.english_crypto as EC

N = 26  # For english letter encoding

def encode(msg, key):
    """
    Encode an english message using a key with the Modified Vigenere Cipher
    :param msg: The message to encode
    :param key: The key to use to encode the message
    :return: The encoded message
    """
    msg_nums = EC.convert_alpha_to_nums(msg)
    key_nums = EC.convert_alpha_to_nums(key)

    n = len(key)
    encoded_msg = []

    cur_msg_index = 0
    cur_key_index = 0


    while cur_msg_index < len(msg):
            encoded_num = (msg_nums[cur_msg_index] + key_nums[cur_key_index]) % N
            cur_key_index = (cur_key_index + 1) % n

            if cur_msg_index >= n:
                encoded_num += (encoded_msg[(cur_msg_index - n)]) % N

            encoded_msg.append(encoded_num)
            cur_msg_index += 1

    encoded_string = EC.convert_nums_to_alpha(encoded_msg)

    return encoded_string