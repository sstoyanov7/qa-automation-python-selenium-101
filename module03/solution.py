import math

def sum_of_digits(n):
    """
    Sum of all digits of a number
    :param n: number
    :return: sum
    """
    digits = to_digits(n)
    sum = 0
    while digits:
        digit = digits.pop()
        sum += digit

    return sum


def to_digits(number):
    """
    Split a number to decimal digits
    :param number: an integer number
    :return: a list of all digits of a number
    """
    reminder = abs(number)
    numbers = []
    while reminder > 0:
        digit = reminder % 10
        numbers.insert(0, digit)
        reminder = reminder // 10

    return numbers


def to_number(digits):
    """
    Convert a list of digits to an integer number
    :param digits: list of digits
    :return: number from concatenated digits
    """
    s = ""
    for f in digits:
        s += str(f)
    number = int(s)
    return number

def count_vowels(str):
    """
    Count upper and lower case vowels in a string
    :param str: string
    :return: count of vowels
    """
    vowels = ["a", "e", "i", "o", "u", "y"]
    s_lower = str.lower()
    count = 0
    for v in vowels:
        c = s_lower.count(v)
        count = count + c

    return count


def count_consonants(str):
    """
    Count upper and lower case consonants in a string
    :param str: string
    :return: count of consonants
    """
    consonants = list("bcdfghjklmnpqrstvwxz")
    count = count_characters(str, consonants)

    return count


def count_characters(str, chars):
    """
    Count characters in a string
    :param str: string
    :param chars: list of characters to be counted
    :return: count of all characters
    """
    s_lower = str.lower()
    count = 0
    for ch in chars:
        c = s_lower.count(ch)
        count = count + c

    return count


def prime_number(number):
    """
    Checks is given number a prime number
    :param number: number to be checked
    :return: True, if it's a primary or False, if it's not
    """
    i = 2
    while i < number:
        if ((number % i) == 0):
            return False
        i += 1
    else:
        return True

def fact_digits(n):
    """
    Sum of the factorials of each digit
    :param n: number
    :return: sum of all factorials of digits
    """
    sum = 0
    digits = to_digits(n)
    for i in digits:
        sum += math.factorial(i)

    return sum


def fibonacci(n):
    """
    List of with the first `n` members of the Fibonacci sequence
    :param n: number
    :return: a list with the first `n` members of the Fibonacci sequence
    """
    if n == 1:
        return [1]

    if n == 2:
        return [1, 1]

    i = 3
    f_list = [1, 1]
    while i <= n:
        f_number = f_list[-2] + f_list[-1]
        f_list.append(f_number)
        i += 1

    return f_list


def fib_number(n):
    """
    A number with digits of first `n` Fibonacci numbers
    :param n: number
    :return: a number, formed by concatenating the first `n` Fibonacci numbers
    """
    f_list = fibonacci(n)
    result = to_number(f_list)

    return result



def palindrome(obj):
    """
    Check is string or a number has symmetrical sequence of elements
    :param obj: integer or string
    :return: True, if elements are symmetrical or False otherwise
    """
    s = str(obj)
    half = int(len(s) / 2)
    for i in range(half):
        left = s[i]
        right = s[-(i+1)]
        if left != right:
            return False

    return True


def char_histogram(string):
    """
    Counts the the number of times each character occurs in a string
    :param string: string to be analyzed
    :return: dictionary with key a character and value the number of occurrences
    """
    dictionary = {}
    for char in list(string):
        dictionary[char] = string.count(char)

    return dictionary

