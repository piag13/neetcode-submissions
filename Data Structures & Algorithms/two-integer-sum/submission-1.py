class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for key, value in enumerate(nums):
            if target - value in hashmap:
                return [hashmap[target - value], key]
            hashmap[value] = key
        return 