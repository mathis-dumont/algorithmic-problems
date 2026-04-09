class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1:
            return False

        min_val = min(nums)
        max_val = max(nums)

        offset = -min_val if min_val < 0 else 0
        size = max_val + offset + 1
        flags = [False] * size

        for num in nums:
            idx = num + offset
            if flags[idx]:
                return True
            flags[idx] = True

        return False