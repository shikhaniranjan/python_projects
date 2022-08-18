class Solution:

    def twoSum(self, nums, target):

        complementMap = dict()
        for i in range(0,len(nums)):
            num =nums[i]
            complement = target - num
            if num in complementMap:
                return [complementMap[num],i]
            else:
                complementMap[complement] = i

'''
        for i in range(0, len(nums)):
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return ([i, j])
                    #print("in while loop")
                    break
                else:
                    continue
'''

nums = [3,2,4]
target = 6
so = Solution()
Two =so.twoSum(nums ,target)
print(Two)