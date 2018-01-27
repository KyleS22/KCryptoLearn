"""
Common useful functions for cryptography in English

Author: Kyle Seidenthal
"""



# Frequencies of english characters in alphabetical order
english_freqs = [('A', 0, 0.0815), ('B', 1, 0.0144), ('C', 2, 0.0276), ('D', 3, 0.0379), ('E', 4, 0.1311),
                 ('F', 5, 0.0292), ('G', 6, 0.0199), ('H', 7, 0.0526), ('I', 8, 0.0635), ('J', 9, 0.0013),
                 ('K', 10, 0.0042), ('L', 11, 0.0339), ('M', 12, 0.0254), ('N', 13, 0.0710), ('O', 14, 0.0800),
                 ('P', 15, 0.0198), ('Q', 16, 0.0012), ('R', 17, 0.0683), ('S', 18, 0.0610), ('T', 19, 0.1047),
                 ('U', 20, 0.0246), ('V', 21, 0.0092), ('W', 22, 0.0154), ('X', 23, 0.0017), ('Y', 24, 0.0198),
                 ('Z', 25, 0.0008)]


def convert_alpha_to_nums(letters):
    """
    Convert a string into a list of corresponding numbers
    :param letters: The string to be encoded
    :return: A list of numbers representing the given string
    """
    numbers = []

    try:
        for letter in letters:
            if not letter == ' ':
                number = convert_alpha_to_num(letter)
                numbers.append(number)

        return numbers
    except:
        print("Invalid string entered.")

def convert_nums_to_alpha(numbers):
    """
    Convert a list of numbers to a list of letters representing a string
    :param numbers: The numbers to be decoded
    :return: A list of letters representing the numbers given
    """
    letters = []

    try:
        for number in numbers:
            number = int(number)
            letter = convert_num_to_alpha(number)
            letters.append(letter)

        return letters
    except:
        print("Invalid list entered.")

def convert_num_to_alpha(number):
    """
    Convert a single number to its alphabet equivalent
    :param number: The number to be decoded
    :return: The corresponding letter in lowercase
    """
    number = number % 26

    number += 97
    letter = chr(number).upper()




    return letter

def convert_alpha_to_num(letter):
    """
    Convert a letter to its numeric equivalent
    :param letter: The letter to be encoded
    :return: The corresponding number
    """

    try:
        letter = letter.lower()
        number = ord(letter) - 97
        return number
    except:
        print("Invalid input.  Must be an english character.")


def get_bool(prompt):
    """
    Force user to enter boolean value
    :param prompt: The prompt for input
    :return: true or false depending on the user's input
    """
    while True:
        try:
            return {"y": True, "n": False}[input(prompt).lower()]
        except KeyError:
            print("Invalid input please enter y or n!")

def get_frequency_count(s):
    """
    Returns a dictionary containing the frequency of each character in s
    :param s: The string to get the frequency of
    :return: A dictionary containing the frequency of each character in s
    """
    freqs = {}

    for letter in s.upper():

        if letter == ' ':
            continue

        if letter in freqs.keys():
            freqs[letter] += 1
        else:
            freqs[letter] = 1

    return freqs

def index_of_coincidence(s):
    """
    Calculates the index of coincidence of s
    :param s: The string to get the index of coincidence for
    :return: The index of coincidence of s
    """
    s = s.replace(" ", "")

    n = len(s)

    freqs = get_frequency_count(s)

    if(n-1) > 0:
        coefficient = 1/(n * (n-1))
    else:
        coefficient = 0

    freq_sum = 0

    for key in freqs.keys():
        freq_sum += freqs[key] * (freqs[key] - 1)

    index = freq_sum * coefficient

    return index

