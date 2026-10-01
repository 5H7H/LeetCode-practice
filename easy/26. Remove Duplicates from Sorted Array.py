class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1 #插入的位置
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]: #对比相邻的数字，如果不同就写入位置k
                nums[k] = nums[i] 
                k = k + 1
        return k