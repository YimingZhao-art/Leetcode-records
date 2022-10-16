class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        myDict = {}
        for i in nums1:
            if i in myDict:
                myDict[i][0] += 1
            else:
                myDict[i] = [1,0]
        List = []
        for each in nums2:
            if each in myDict:
                myDict[each][1] += 1
        for each in myDict:
            if myDict[each][1] != 0:
                List += [each]*(min(myDict[each][0], myDict[each][1]))
        return List