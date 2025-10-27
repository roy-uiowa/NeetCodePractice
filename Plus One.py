class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        def add(digit, n):
            if di
            return val%10, val//10
        carry = 0
        p = 0
        for i in range(len(digits)-1, -1, -1):
            if i == len(digits)-1:
                digits[i], carry = add(digits[i], 1)
            else:
                digits[i], carry = add(digits[i], carry)
        if carry == 1: digits = [carry] + digits
        return digits
