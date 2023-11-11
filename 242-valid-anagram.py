class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False
        



x = Solution()
s = "rat"
t = "car"

print(x.isAnagram(s, t))