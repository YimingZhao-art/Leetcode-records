class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        myDict = {}
        for i in range(len(nums)):
            if nums[i] not in myDict:
                myDict[nums[i]] = i
            else:
                if i-myDict[nums[i]] <= k:
                    return True
                else:
                    myDict[nums[i]] = i
        return False
            