class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        myDict = {}
        for i in set1:
            myDict[i] = 1
        List = []
        for each in set2:
            if each in myDict:
                List.append(each)
        return List