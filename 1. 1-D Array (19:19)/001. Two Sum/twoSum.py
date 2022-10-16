class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictHashmap = dict()
        for i in range(len(nums)):
            dictHashmap[nums[i]] = i
        for i in range(len(nums)):
            if target-nums[i] in dictHashmap and i!=dictHashmap[target-nums[i]]:
                return [i, dictHashmap[target-nums[i]]]
            
        