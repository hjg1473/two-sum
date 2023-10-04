from typing import List
def twoSum(self, nums: List[int], target: int) -> List[int]:
    result = []
    length = len(nums)
    for i in range(length):
        for j in range(length):
            if (nums[i] + nums[j] == target):
                result.append(i)
                result.append(j)
                print(result)
                break;
# YOUR ANSWER
return