class Solution:
    def nextPermutation(self, num: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dropPoint = -1
        for i in range(len(num)-1, 0, -1):
            if num[i] > num[i-1]:
                dropPoint = i-1
                break
        movable = num[dropPoint+1:]
        p=0
        for i in range(len(num)-1, dropPoint, -1):
            num[i] = movable[p]
            p+=1
        
        tag = dropPoint
        for i in range(len(num[dropPoint+1:])):
            if num[dropPoint+1+i] > num[dropPoint]:
                tag = dropPoint+1+i
                break
        print(dropPoint, tag)
        print(num[dropPoint], num[tag])
        num[dropPoint], num[tag] = num[tag], num[dropPoint]