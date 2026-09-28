from text_tools import count_words, is_palindrome
from datetime import date

if __name__ == "__main__":
    # Get input from user
    sentence = input("Please enter a sentence: ")

    # Print word count
    print(f"The sentence contains {count_words(sentence)} words.")

    # Check if the sentence is a palindrome
    print("Is it a palindrome? ", is_palindrome(sentence))
    # Print current date
    print("Today's date is:", date.today())