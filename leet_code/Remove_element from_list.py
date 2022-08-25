class Solution:
    def removeElement(self, nums, val):
        nums = [ele for ele in nums if ele !=val]
        return (len(nums))

nums = [3,2,2,3]
val = 3
