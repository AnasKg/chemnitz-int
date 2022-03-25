
"""
    2. Write an algorithm that recalculates the
    characters of your name (e.g. Latin alphabet, Klingon, whatever you like)
    into a integer value (A = 1, B = 2, …) and sums up all the values.

    Solution:
    This problem has several solutions.
    The first solution is to use an array of characters,
    where the characters are letters of the Latin alphabet,
    and the indexes of the elements of the array are the integer value of the letter.

    The second solution is to use the asc value of the character.
    For example the ascii code of character 'a' is 97, 'b'=98 ... 'z'=122.
    Let's take any name, for example 'anas', write down the ascii code of each character
        a = 97
        n = 110
        a = 97
        s = 115
    We decrease the ascii code by 96 and as a result we get the integer value of this letter in the alphabet.
        a = 97 - 96 = 1
        n = 110 - 96 = 14
        a = 97 - 96 = 1
        s = 115 - 96 = 19

    In total we get 35
"""


def recalculate_character_of_name(name: str) -> int:
    """
    :param name: string contains only latin alphabet
    :return: sum of the characters name
    """
    lower_name = name.lower()
    ascii_start = 96
    sum = 0
    for symbol in lower_name:
        ascii_value = ord(symbol)
        integer_value = ascii_value - ascii_start
        res = f'{symbol} -> {integer_value}'
        print(res)
        sum += integer_value

    return sum


if __name__ == '__main__':
    name = input('Input your name: ')
    if not name.isalpha():
        print('Name must be contain only latin alphabet!')
    else:
        sum = recalculate_character_of_name(name)
        print('The sum of the characters of your name: ', sum)
