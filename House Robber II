class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_house(houses):
            prev2, prev1 = 0, 0
            for i in range(len(houses)):
                rob_this = max(houses[i] + prev2 , prev1)
                prev2 = prev1
                prev1 = rob_this
            return prev1
        
        if len(nums) == 1: return nums[0]
        return max(rob_house(nums[:-1]), rob_house(nums[1:]))
