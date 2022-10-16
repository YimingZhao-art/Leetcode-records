from typing import List
class Solution:
    def check(self, nums, largest, left, right) -> int:
        count = 0
        while left < right:
            sum = nums[left] + nums[right]
            if sum > largest:
                count += right-left
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                left += 1
            else:
                while right < left and nums[right] == nums[right-1]:
                    right -= 1
                right -= 1
        return count
    
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        print(nums)
        
        count = 0
        
        for i in range(len(nums)-1):
            count += self.check(nums, nums[i], i+1, len(nums)-1)
        
        
        
        
        return count
    
sol = Solution()
a = sol.triangleNumber([2,2,3,4])
print(a)