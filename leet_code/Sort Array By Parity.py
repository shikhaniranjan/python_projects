class Solution:
    def sortArrayByParity(self, nums):
        even = 0
        odd = len(nums)-1
        while (even<odd):
            if (nums[even]%2==0 and even < odd):
                even+=1
            elif (nums[odd]%2!=0 and even < odd):
                odd-=1
            else:
                nums[even],nums[odd]=nums[odd],nums[even]
        return nums
nums = [3,1,2,4]
Sol =Solution()
sort_parity = Sol.sortArrayByParity(nums)
print(sort_parity)