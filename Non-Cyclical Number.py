class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSqrs(num):
            output = 0
            while num:
                output += (num%10)**2
                num = num//10
            return output 

        slow, fast = n, sumOfSqrs(n)
        while slow != fast:
            fast = sumOfSqrs(fast)
            fast = sumOfSqrs(fast)
            slow = sumOfSqrs(slow)
        return True if fast == 1 else False
                
