class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        is_duplicate = False
        h_map = {}
        for i in nums:
            if i not in h_map:
                h_map[i] = 1
            else:
                is_duplicate = True
                break
        return is_duplicate
        