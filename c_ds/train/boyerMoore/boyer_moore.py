import unittest

# Assuming your boyer_moore_search function is defined here
# For demonstration purposes, I'll include a placeholder.
# You would replace this with your actual Boyer-Moore implementation.
import time

class BoyerMoore:
    def __init__(self, pattern, log = False):
        self.pattern = pattern
        self.m = len(pattern)
        self.alphabet = set(pattern)
        self._bad_character_table()
        self.log = log

    def _bad_character_table(self):
        self._bad_char  = {}
        for index in range(self.m):
            self._bad_char[ord(self.pattern[index])] = index
    def _get_bad_char_index(self, bad_char):
        if ord(bad_char) in self._bad_char.keys():
            return self._bad_char[ord(bad_char)]
        else:
            return -1

    def search(self, text):
        result = []
        n = len(text)
        if n < self.m:
            result.append(-1)
            return result
        s = 0 
        while s <= n - self.m:
            # substring to compare = text[s:s+m-1]
            char_offset = self.m -1
            text_offset = s + char_offset
            while char_offset >= 0 and text[text_offset] == self.pattern[char_offset]:
                char_offset -= 1
                text_offset -= 1
            
            if self.log is True:
                print(f"\t s:{s} -- char_offset:{char_offset}")
            if char_offset < 0:
                result.append(s)
                s += 1
            else:
                bad_char_offset = self._get_bad_char_index(text[text_offset])
                shift = max(char_offset - bad_char_offset, 1)
                s += shift
                if self.log is True:
                    print(f"\t bad_char:{text[text_offset]} != {self.pattern[char_offset]} \t s:{s} \t offset:{bad_char_offset} \t {text}")
            # time.sleep(0.5)
        if len(result) == 0 :
            result.append(-1)
        return result 

def search(txt, pat):
    bm = BoyerMoore(pat, True)
    result = bm.search(txt)
    print(f"pattern:{pat}")
    print(f"text:{txt}")
    return result

def boyer_moore_search(txt, pattern):
    """
    Placeholder for the Boyer-Moore search algorithm.
    You will replace this with your actual implementation.
    This basic version just uses Python's find() for demonstration.
    """
    bm = BoyerMoore(pattern)
    result = bm.search(txt)
    print(f"\ttext:{txt}")
    print(f"\tpattern:{pattern}")
    print(f"\tresult:{result}")
    time.sleep(0.10)
    return result[0]
    # return text.find(pattern)


class TestBoyerMoore(unittest.TestCase):

    def test_pattern_at_beginning(self):
        text = "apple pie"
        pattern = "apple"
        self.assertEqual(boyer_moore_search(text, pattern), 0)

    def test_pattern_in_middle(self):
        text = "this is a test string"
        pattern = "test"
        self.assertEqual(boyer_moore_search(text, pattern), 10)

    def test_pattern_at_end(self):
        text = "hello world"
        pattern = "world"
        self.assertEqual(boyer_moore_search(text, pattern), 6)

    def test_pattern_not_found(self):
        text = "abcdefg"
        pattern = "xyz"
        self.assertEqual(boyer_moore_search(text, pattern), -1)

    def test_empty_text(self):
        text = ""
        pattern = "abc"
        self.assertEqual(boyer_moore_search(text, pattern), -1)

    def test_empty_pattern(self):
        text = "some text"
        pattern = ""
        # Conventionally, an empty pattern is found at index 0.
        # This might vary based on your specific requirements.
        self.assertEqual(boyer_moore_search(text, pattern), 0)

    def test_empty_text_and_pattern(self):
        text = ""
        pattern = ""
        self.assertEqual(boyer_moore_search(text, pattern), 0)

    def test_single_character_pattern(self):
        text = "abcde"
        pattern = "c"
        self.assertEqual(boyer_moore_search(text, pattern), 2)

    def test_single_character_pattern_not_found(self):
        text = "abcde"
        pattern = "z"
        self.assertEqual(boyer_moore_search(text, pattern), -1)

    def test_pattern_longer_than_text(self):
        text = "short"
        pattern = "verylongpattern"
        self.assertEqual(boyer_moore_search(text, pattern), -1)

    def test_pattern_with_spaces(self):
        text = "this has some spaces in it"
        pattern = "some spaces"
        self.assertEqual(boyer_moore_search(text, pattern), 9)

    def test_pattern_with_special_characters(self):
        text = "abc!@#$xyz"
        pattern = "!@#"
        self.assertEqual(boyer_moore_search(text, pattern), 3)

    def test_multiple_occurrences_first_one(self):
        text = "ababab"
        pattern = "aba"
        self.assertEqual(boyer_moore_search(text, pattern), 0)

    def test_overlapping_pattern(self):
        text = "AAAAA"
        pattern = "AAA"
        self.assertEqual(boyer_moore_search(text, pattern), 0)

    def test_unicode_characters(self):
        text = "你好世界"
        pattern = "世界"
        self.assertEqual(boyer_moore_search(text, pattern), 2)

    def test_case_sensitivity(self):
        text = "Hello World"
        pattern = "world"
        self.assertEqual(boyer_moore_search(text, pattern), -1) # Assuming case-sensitive

    def test_case_sensitivity_match(self):
        text = "Hello World"
        pattern = "World"
        self.assertEqual(boyer_moore_search(text, pattern), 6)

    def test_long_text_and_pattern(self):
        text = "A" * 1000 + "B" + "A" * 1000
        pattern = "B"
        self.assertEqual(boyer_moore_search(text, pattern), 1000)

    def test_pattern_at_start_of_very_long_text(self):
        text = "test" + "X" * 100000
        pattern = "test"
        self.assertEqual(boyer_moore_search(text, pattern), 0)


def test():
    txt = "abcdefg"
    pat = "xyz"
    print(f"{search(txt, pat)}\n--")
    txt = "ABAAABCDABC,ABC"
    print(f"{search(txt, pat)}\n--")
    txt = "ABCAABCDABC,ABC"
    print(f"{search(txt, pat)}\n--")
    txt = "ABCAABCDBBCZABC"
    print(f"{search(txt, pat)}\n--")
    print(f"{search(txt, "ABCD")}\n--")
    text = "Hello World"
    pattern = "world"
    print(f"{search(text, pattern)}\n--")

def all_tests():
# if __name__ == '__main__':
    # To run these tests, replace the placeholder boyer_moore_search
    # with your actual Boyer-Moore implementation.
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

# def old_main():
if __name__ == "__main__":
    import sys
    from boyer_moore import BoyerMoore

    # Example usage
    if len(sys.argv) != 3:
        test()
        all_tests()
        exit(0)

    pattern = sys.argv[1]
    text = sys.argv[2]

    bm = BoyerMoore(pattern)
    result = bm.search(text)

    if result != -1:
        print(f"Pattern found at index: {result}")
    else:
        print("Pattern not found.")

