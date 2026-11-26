class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {target-nums[i]: i for i in range(len(nums))}
        for i in range(len(nums)) :
            if nums[i] in hash :
                if i != hash[nums[i]]:
                    return [i,hash[nums[i]]]


        