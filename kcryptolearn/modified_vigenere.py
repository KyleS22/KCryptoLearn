"""
Implementation of the Modified Vigenere Cipher

Author: Kyle Seidenthal
"""
import kcryptolearn.english_crypto as ec
import math

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

def get_key_length(msg, tolerance=0.06):
    """
    Determine the possible key length of the message encoded with modified vigenere.
    Note that this length can be wrong, but it is likely that the actual key length divides this number
    or is a multiple of it.

    Not so good on small ciphertext lengths

    :param msg: The message to get the key length for
    :param tolerance: How close to english the text should be before stopping
    :return: The length of the key used to encode msg
    """
    msg_nums = ec.convert_alpha_to_nums(msg)

    k = 1       # initial key guess

    while k < (len(msg_nums)):

        new_text = []

        cur_msg_index = 0

        while cur_msg_index < len(msg_nums):
                if cur_msg_index < k:
                    new_text.append(msg_nums[cur_msg_index])    # If we are still on the first use of key, don't change
                else:
                    # Subtract the previous kth character from this one to get a regular vigenere
                    new_letter = msg_nums[cur_msg_index] - msg_nums[(cur_msg_index - k)]
                    new_text.append(new_letter)

                cur_msg_index += 1

        # Convert to text
        new_text_string = ec.convert_nums_to_alpha(new_text)

        # Now we split the text into k groups; each with every kth letter from the start letter
        strings = ['']*k

        for i in range(len(new_text_string)):
            strings[(i % k)] += new_text_string[i]

        ind_cos = [0]*k

        # Calculate index of coincidence for each sub-string
        cur_index = 0
        for string in strings:
            ind_cos[cur_index] = ec.index_of_coincidence(string)
            cur_index += 1

        # Get the average index and see if it is close to english
        avg_index = sum(ind_cos)/len(ind_cos)

        if avg_index >= tolerance:
            return k

        k += 1

    return -1


# TODO Find a good algorithm for breaking this encryption


