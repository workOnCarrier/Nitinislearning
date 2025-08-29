
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digit_pos = len(digits) - 1
        carry = 1
        while digit_pos >= 0 and carry == 1:
            new_carry = (digits[digit_pos] + 1) / 10
            digits[digit_pos] =  (digits[digit_pos] + carry) % 10
            carry = new_carry
            digit_pos -= 1
        if carry == 1:
            result = [1]
            result += digits
            return result
        return digits


        
def main ():
    input_1 = [1,2,3]
    input_2 = [9]
    input_3 = [4, 3, 2, 1]
    s = Solution()
    print(s.plusOne(input_1))
    print(s.plusOne(input_2))
    print(s.plusOne(input_3))


if __name__ == "__main__":
    main()