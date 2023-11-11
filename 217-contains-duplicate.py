class Solution:
    def containsDuplicate(self, nums) -> bool:
        deduplicated = set(nums)

        if len(deduplicated) != len(nums):
            return True
        else:
            return False
        


x = Solution()
nums = [1,1,1,3,3,4,3,2,4,2]

print(x.containsDuplicate(nums))