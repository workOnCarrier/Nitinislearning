class Solution:
    def findLength(self, str1, k):
        window_start, max_length, max_repeat_letter_count = 0, 0, 0
        frequency_map = {}

        # Try to extend the range [window_start, window_end]
        for window_end in range(len(str1)):
            right_char = str1[window_end]
            if right_char not in frequency_map:
                frequency_map[right_char] = 0
            frequency_map[right_char] += 1

            # we don't need to place the maxRepeatLetterCount under the below 'if', see the
            # explanation in the 'Solution' section above.
            max_repeat_letter_count = max(
                max_repeat_letter_count, frequency_map[right_char])

            # Current window size is from window_start to window_end, overall we have a letter
            # which is repeating 'max_repeat_letter_count' times, this means we can have a window
            # which has one letter repeating 'max_repeat_letter_count' times and the remaining
            # letters we should replace. If the remaining letters are more than 'k', it is the
            # time to shrink the window as we are not allowed to replace more than 'k' letters
            if (window_end - window_start + 1 - max_repeat_letter_count) > k:
                left_char = str1[window_start]
                frequency_map[left_char] -= 1
                window_start += 1

            max_length = max(max_length, window_end - window_start + 1)
        return max_length


def main():
    sol = Solution()
    print(sol.findLength("aabccbb", 2))
    print(sol.findLength("abbcb", 1))
    print(sol.findLength("abccde", 1))


main()
