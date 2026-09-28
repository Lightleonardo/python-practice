def count_words(text):
    """
    Returns the number of words in the given string.

    Parameters:
    text (str): The string to count the words in.

    Returns:
    int: The number of words in the string.
    """
    return len(text.split())

def is_palindrome(text):
    """
    Returns True if the string is a palindrome, False otherwise.

    Parameters:
    text (str): The string to check.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    return text.lower().replace(" ", "") == text.lower().replace(" ", "")[::-1]
