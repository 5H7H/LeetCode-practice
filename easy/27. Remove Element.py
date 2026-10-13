class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        i = len(nums) - 1
        while k <= i:
            if nums[k] == val:
                while k <= i and nums[i] == val:
                    i -= 1
                nums[k] = nums[i]
                i -= 1
            k += 1

        return k