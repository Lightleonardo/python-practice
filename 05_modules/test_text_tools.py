import text_tools
import unittest

class TestTextTools(unittest.TestCase):

    def test_count_words_normal_sentence(self):
        # Test with a normal sentence
        text = "The quick brown fox jumps over the lazy dog"
        self.assertEqual(text_tools.count_words(text), 9)

    def test_count_words_empty_string(self):
        # Test with an empty string
        text = ""
        self.assertEqual(text_tools.count_words(text), 0)

    def test_is_palindrome(self):
        # Test with a palindrome sentence
        text = "Never odd or even"
        self.assertEqual(text_tools.is_palindrome(text), True)

        # Test with a non-palindrome sentence
        text = "hello"
        self.assertEqual(text_tools.is_palindrome(text), False)

    def test_is_palindrome_with_spaces(self):
        # Test with a sentence with spaces
        text = "A man, a plan, a canal, Panama"
        self.assertEqual(text_tools.is_palindrome(text), False)

        # Test with a sentence without spaces
        text = "A man, a plan, a canal"
        self.assertEqual(text_tools.is_palindrome(text), False)

if __name__ == "__main__":
    unittest.main()