class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        LP = 0
        RP = len(nums) - 1
        while True:
            if nums[(RP - LP) // 2 + LP]  > target:
                RP = (RP - LP) // 2 + LP
            else:
                LP = (RP - LP) // 2 + LP

