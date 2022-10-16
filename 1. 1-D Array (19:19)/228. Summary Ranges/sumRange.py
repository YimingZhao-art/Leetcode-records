from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        answer = []
        if len(nums) < 2:
            if len(nums) == 1:
                return [str(nums[0])]
            else:
                return []
        else:
            start = nums[0]
            end = nums[0]
            for i in range(1, len(nums)):
                # print(nums[i])
                if nums[i] - nums[i-1] != 1:
                    if start != end:
                        answer.append(f"{start}->{end}")
                    else:
                        answer.append(f"{start}")
                    start = nums[i]
                    end = nums[i]
                else:
                    end += 1
            if start != end:
                answer.append(f"{start}->{end}")
            else:
                answer.append(f"{start}")
            return answer