class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        wSize = len(s1)
        charS1 = {}
        for i in s1:
            charS1[i] = 1+charS1.get(i, 0)
        for i in range(len(s2)-wSize+1):
            charS2 = {}
            for j in range(i, i+wSize):
                charS2[s2[j]] = 1+charS2.get(s2[j], 0)
            if charS2 == charS1: return True
        return False
