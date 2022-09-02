class Solution:
    def removeElement(self, nums, val):
        from pdb import set_trace
        set_trace()
        nums = [ele for ele in nums if ele !=val]
        return (nums)

nums = [3,2,2,3]
val = 3
Sol =Solution()
res = Sol.removeElement(nums,val)
print(res)
