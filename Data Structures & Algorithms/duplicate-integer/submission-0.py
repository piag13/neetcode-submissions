class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        contains_duplicate = set(nums)
        if len(nums) != len(contains_duplicate):
            return True
        else:
            return False