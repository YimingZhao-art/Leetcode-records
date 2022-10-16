class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        myDict = {}
        for i in range(len(nums)):
            if nums[i] not in myDict:
                myDict[nums[i]] = i
            else:
                return True
        return False